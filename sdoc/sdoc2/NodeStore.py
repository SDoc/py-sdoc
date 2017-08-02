"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------

inline_creators = {}
"""
Map from inline commands to node creators.

:type: dict[str,callable]
"""

block_creators = {}
"""
Map from block commands to object creators.

:type: dict[str,callable]
"""

formatters = {}
"""
Map from format name to map from inline and block commands to format creators.

:type: dict[str,dict[str,callable]]
"""


class NodeStore:
    """
    Class for creating, storing, and retrieving nodes.

    @todo Make abstract and implement other document store classes.
    """

    _errors = 0
    """
    The error count.

    :type: int
    """

    _io = None
    """
    Styled output formatter.

    :type: None|sdoc.style.SdocStyle.SdocStyle
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io):
        """
        Object constructor.
        """
        NodeStore._io = io

        self.format = 'html'
        """
        The output format.

        :type: str
        """

        self.nested_nodes = []
        """
        The stack of nested nodes (only filled when creating all nodes).

        :type: list[sdoc.sdoc2.node.Node.Node]
        """

        self.nodes = {}
        """
        The actual node store. Map from node ID to node.

        :type: dict[int,sdoc.sdoc2.node.Node.Node]
        """

        self._enumerable_numbers = {}
        """
        The current numbers of enumerable nodes (e.g. headings, figures).

        :type: dict[str,sdoc.sdoc2.helper.Enumerable.Enumerable]
        """

        self.labels = {}
        """
        The identifiers of labels which refers on each heading node.

        :type: dict[str,str]
        """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def error(message, node=None):
        """
        Logs an error.

        :param str message: The error message.this message will be appended with 'at filename:line.column' ot the token.
        :param sdoc.sdoc2.node.Node.Node node: The node where the error occurred.
        """
        NodeStore._errors += 1

        messages = [message]
        if node:
            filename = node.position.file_name
            line_number = node.position.start_line
            column_number = node.position.start_column + 1
            messages.append('Position: {0!s}:{1:d}.{2:d}'.format(filename, line_number, column_number))
        NodeStore._io.error(messages)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_formatter(output_type, name_formatter):
        """
        Returns the formatter for special type.

        :param str output_type: The type of output formatter (e.g. 'html')
        :param str name_formatter: The name of formatter (e.g. 'smile')

        :rtype: sdoc.sdoc2.formatter.Formatter.Formatter
        """
        return formatters[output_type][name_formatter]

    # ------------------------------------------------------------------------------------------------------------------
    def end_block_node(self, command):
        """
        Signals the end of a block command.

        :param string command: The name of the inline command.
        """
        # Pop none block command nodes from the stack.
        while self.nested_nodes and not self.nested_nodes[-1].is_block_command():
            self.nested_nodes.pop()

        if not self.nested_nodes:
            # @todo position
            raise RuntimeError("Unexpected \\end{{{0!s}}}.".format(command))

        # Get the last node on the block stack.
        node = self.nested_nodes[-1]

        if node.name != command:
            # @todo position \end
            # @todo position \begin
            raise RuntimeError("\\begin{{{0!s}}} and \\end{{{1!s}}} do not match.".format(node.name, command))

        # Pop the last node of the block stack.
        self.nested_nodes.pop()

    # ------------------------------------------------------------------------------------------------------------------
    def in_scope(self, node_id):
        """
        Retrieves a node based on its ID.

        :param int node_id: The node ID.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        return self.nodes[node_id]

    # ------------------------------------------------------------------------------------------------------------------
    def out_scope(self, node):
        """
        Marks a node as not longer in scope.

        :param sdoc.sdoc2.node.Node.Node node: The node.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def register_inline_command(command, constructor):
        """
        Registers a node constructor for an inline command.

        :param str command: The name of the inline command.
        :param callable constructor: The node constructor.
        """
        inline_creators[command] = constructor

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def register_formatter(command, output_format, formatter):
        """
        Registers a output formatter constructor for a command.

        :param str command: The name of the command.
        :param str output_format: The output format the formatter generates.
        :param callable formatter: The formatter for generating the content of the node in the output format.
        """
        if output_format not in formatters:
            formatters[output_format] = {}

        formatters[output_format][command] = formatter

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def register_block_command(command, constructor):
        """
        Registers a node constructor for a block command.

        :param string command: The name of the inline command.
        :param callable constructor: The node constructor.
        """
        block_creators[command] = constructor

    # ------------------------------------------------------------------------------------------------------------------
    def create_inline_node(self, command, options=None, argument='', position=None):
        """
        Creates a node based an inline command.

        Note: The node is not stored nor appended to the content tree.

        :param str command: The inline command.
        :param None|dict[str,str] options: The options.
        :param str argument: The argument of the inline command.
        :param None|sdoc.sdoc2.Position.Position position: The position of the node definition.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        if command not in inline_creators:
            # @todo set error status
            constructor = inline_creators['unknown']
            node = constructor(self._io, options, argument)
            node.name = command

        else:
            # Create the new node.
            constructor = inline_creators[command]
            node = constructor(self._io, options, argument)

        node.position = position

        # Store the node and assign ID.
        self.store_node(node)

        return node

    # ------------------------------------------------------------------------------------------------------------------
    def create_block_node(self, command, options, position=None):
        """
        Creates a node based on a block command.

        Note: The node is not appended to the content tree.

        :param str command: The inline command.
        :param dict[str,str] options: The options.
        :param None|sdoc.sdoc2.Position.Position position: The position of the node definition.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        if command not in block_creators:
            constructor = block_creators['unknown']
            # @todo set error status

        else:
            # Create the new node.
            constructor = block_creators[command]

        node = constructor(self._io, options)
        node.position = position

        # Store the node and assign ID.
        self.store_node(node)

        return node

    # ------------------------------------------------------------------------------------------------------------------
    def append_inline_node(self, command, options, argument, position):
        """
        Creates a node based an inline command and appends it to the end of the content tree.

        :param str command: The inline command.
        :param dict[str,str] options: The options.
        :param str argument: The argument of the inline command.
        :param sdoc.sdoc2.Position.Position position: The position of the node definition.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        # Create the inline node.
        node = self.create_inline_node(command, options, argument, position)

        # Add the node to the node store.
        self._append_to_content_tree(node)

        return node

    # ------------------------------------------------------------------------------------------------------------------
    def append_block_node(self, command, options, position):
        """
        Creates a node based on a block command and appends it to the end of the content tree.

        :param str command: The inline command.
        :param dict[str,str] options: The options.
        :param sdoc.sdoc2.Position.Position position: The position of the node definition.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        # Create the block node.
        node = self.create_block_node(command, options, position)

        # Add the node to the node store.
        self._append_to_content_tree(node)

        return node

    # ------------------------------------------------------------------------------------------------------------------
    def create_formatter(self, io, command, parent=None):
        """
        Creates a formatter for generating the output of nodes in the requested output format.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        :param str command: The inline of block command.
        :param sdoc.sdoc2.formatter.Formatter.Formatter parent: The parent formatter.

        :rtype: sdoc.sdoc2.formatter.Formatter.Formatter
        """
        if self.format not in formatters:
            raise RuntimeError("Unknown output format '{0!s}'.".format(self.format))

        if command not in formatters[self.format]:
            # @todo use default none decorator with warning
            raise RuntimeError("Unknown formatter '{0!s}' for format '{1!s}'.".format(command, self.format))

        constructor = formatters[self.format][command]
        formatter = constructor(io, parent)

        return formatter

    # ------------------------------------------------------------------------------------------------------------------
    def _adjust_hierarchy(self, node):
        """
        Adjust the hierarchy based on the hierarchy of a new node.

        :param sdoc.sdoc2.node.Node.Node node: The new node.
        """
        node_hierarchy_name = node.get_hierarchy_name()
        parent_found = False
        while self.nested_nodes and not parent_found:
            parent_node = self.nested_nodes[-1]
            parent_hierarchy_name = parent_node.get_hierarchy_name()
            if parent_hierarchy_name != node_hierarchy_name:
                if node.is_hierarchy_root():
                    parent_found = True
                else:
                    self.error("Improper nesting of node '{0!s}' at {1!s} and node '{2!s}' at {3!s}.".format(
                        parent_node.name, parent_node.position, node.name, node.position))

            if not parent_found:
                parent_hierarchy_level = parent_node.get_hierarchy_level()
                node_hierarchy_level = node.get_hierarchy_level(parent_hierarchy_level)
                if parent_hierarchy_level >= node_hierarchy_level and len(self.nested_nodes) > 1:
                    self.nested_nodes.pop()
                else:
                    parent_found = True

        parent_node = self.nested_nodes[-1]
        parent_hierarchy_level = parent_node.get_hierarchy_level()
        node_hierarchy_level = node.get_hierarchy_level(parent_hierarchy_level)

        if node_hierarchy_level - parent_hierarchy_level > 1:
            self.error("Improper nesting of levels:{0:d} at {1!s} and {2:d} at {3!s}.".format(
                parent_hierarchy_level, parent_node.position, node_hierarchy_level, node.position),
                node)

    # ------------------------------------------------------------------------------------------------------------------
    def store_node(self, node):
        """
        Stores a node. If the node was not stored before assigns an ID to this node, otherwise the node replaces the
        node stored under the same ID. Returns the ID if the node.

        :param sdoc.sdoc2.node.Node.Node node: The node.

        :rtype: int
        """
        if not node.id:
            # Add the node to the node store.
            node_id = len(self.nodes) + 1
            node.id = node_id

        self.nodes[node.id] = node

        return node.id

    # ------------------------------------------------------------------------------------------------------------------
    def _append_to_content_tree(self, node):
        """
        Appends the node at the proper nesting level at the end of the content tree.

        :param sdoc.sdoc2.node.Node.Node node: The node.
        """
        if node.id == 1:
            # The first node must be a document root.
            if not node.is_document_root():
                # @todo position of block node.
                raise RuntimeError("Node {0!s} is not a document root".format(node.name))

            self.nested_nodes.append(node)

        else:
            # All other nodes must not be a document root.
            if node.is_document_root():
                # @todo position of block node.
                raise RuntimeError("Unexpected {0!s}. Node is document root".format(node.name))

            # If the node is a part of a hierarchy adjust the nested nodes stack.
            if node.get_hierarchy_name():
                self._adjust_hierarchy(node)

            # Add the node to the list of child nodes of its parent node.
            if self.nested_nodes:
                parent_node = self.nested_nodes[-1]

                # Pop from stack if we have two list element nodes (e.g. item nodes) in a row.
                if node.is_list_element() and type(parent_node) == type(node):
                    self.nested_nodes.pop()
                    parent_node = self.nested_nodes[-1]

                parent_node.child_nodes.append(node.id)

            # Block commands and hierarchical nodes must be appended to the nested nodes.
            if node.is_block_command() or node.get_hierarchy_name():
                self.nested_nodes.append(node)

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares after parsing at SDoc2 level the content tree for further processing.
        """
        # Currently, node with ID 1 is the document node. @todo Improve getting the document node.
        self.nodes[1].prepare_content_tree()

    # ------------------------------------------------------------------------------------------------------------------
    def number_numerable(self):
        """
        Numbers all numerable nodes such as chapters, sections, figures, and, items.
        """
        self.nodes[1].number(self._enumerable_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_toc(self):
        """
        Checks if we have table of contents in document. If yes, we generate table of contents.
        """
        for node in self.nodes.values():
            if node.get_command() == 'toc':
                node.generate_toc()

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate(target_format):
        """
        Generates the document.

        :param sdoc.format.Format.Format target_format: The format which will generate file.
        """
        # Start generating file using specific formatter and check the errors.
        format_errors = target_format.generate()

        NodeStore._errors += format_errors

        return NodeStore._errors

    # ------------------------------------------------------------------------------------------------------------------
    def get_enumerated_items(self):
        """
        Returns a list with tuples with command and number of enumerated nodes.

        This method is intended for unit test only.

        :rtype: list[(str,str)]
        """
        return self.nodes[1].get_enumerated_items()

    # ------------------------------------------------------------------------------------------------------------------
    def parse_labels(self):
        """
        Method for parsing labels, setting additional arguments to nodes, and removing label nodes from tree.
        """
        self.nodes[1].parse_labels()
        self.nodes[1].change_ref_argument()

# ----------------------------------------------------------------------------------------------------------------------
