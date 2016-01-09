"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""

# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import CONTENT_TYPE_SECTION


class NodeStore:
    """
    Class for creating, storing, and retrieving nodes.

    @todo Make abstract
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        self.inline_creators = {}
        """
        Map from inline commands to object creators.

        :type: dict[str,callable]
        """

        self.block_creators = {}
        """
        Map from block commands to object creators.

        :type: dict[str,callable]
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
            raise RuntimeError("Unexpected \\end{%s}." % command)

        # Get the last node on the block stack.
        node = self.nested_nodes[-1]

        if node.name != command:
            # @todo position \end
            # @todo position \begin
            raise RuntimeError("\\begin{%s} and \\end{%s} do not match." % (node.name, command))

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
    def register_inline_command(self, command, constructor):
        """
        Registers a node constructor for an inline command.

        :param string command: The name of the inline command.
        :param callable constructor: The node constructor.
        """
        self.inline_creators[command] = constructor

    # ------------------------------------------------------------------------------------------------------------------
    def register_block_command(self, command, constructor):
        """
        Registers a node constructor for a block command.

        :param string command: The name of the inline command.
        :param callable constructor: The node constructor.
        """
        self.block_creators[command] = constructor

    # ------------------------------------------------------------------------------------------------------------------
    def create_inline_node(self, command, options, argument):
        """
        Creates a node based on a inline command.
        :param str command: The inline command.
        :param dict options: The options.
        :param str argument: The argument of the inline command.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        if command not in self.inline_creators:
            # @todo position
            raise RuntimeError("Unknown inline command '%s'." % command)

        # Create the new node.
        constructor = self.inline_creators[command]
        node = constructor()
        node.argument = argument

        # Add the node to the node store.
        node_id = len(self.nodes) + 1
        node.id = node_id
        self.nodes[node_id] = node

        # If the node is a section node adjust the nested nodes stack.
        # @todo refactor
        if CONTENT_TYPE_SECTION in node.get_content_categories():
            level = node.get_heading_level()
            found_parent = False
            while self.nested_nodes and not found_parent:
                parent_node = self.nested_nodes[-1]
                if CONTENT_TYPE_SECTION not in parent_node.get_content_categories():
                    # @todo position of this node
                    # @todo position of block node.
                    raise RuntimeError("Improper nesting of block node '%s' and section node '%s'." %
                                       (parent_node.name, node.name))

                parent_level = parent_node.get_heading_level()
                if parent_level >= level and parent_level != 0:
                    self.nested_nodes.pop()
                else:
                    found_parent = True

            if self.nested_nodes:
                parent_node = self.nested_nodes[-1]
                parent_level = parent_node.get_heading_level()
            else:
                parent_level = -1

            if level - parent_level > 1:
                # @todo position
                print("Warning improper nesting of section nodes: %d %d." % (parent_level, level))

            if self.nested_nodes:
                parent_node = self.nested_nodes[-1]
                parent_node.nodes.append(node_id)

            self.nested_nodes.append(node)

        else:
            # Add the node to the list of child nodes of its parent node.
            if self.nested_nodes:
                parent_node = self.nested_nodes[-1]
                parent_node.nodes.append(node_id)

    # ------------------------------------------------------------------------------------------------------------------
    def create_block_node(self, command, options):
        """
        Creates a node based on a inline command.
        :param str command: The inline command.
        :param dict options: The options.

        :rtype: sdoc.sdoc2.node.Node.Node
        """
        if command not in self.block_creators:
            # @todo position
            raise RuntimeError("Unknown block command '%s'." % command)

        # Create the new node.
        constructor = self.block_creators[command]
        node = constructor()

        # Add the node to the node store.
        node_id = len(self.nodes) + 1
        node.id = node_id
        self.nodes[node_id] = node

        # Add the node to the list of child nodes of its parent node.
        if self.nested_nodes:
            parent_node = self.nested_nodes[-1]
            parent_node.nodes.append(node_id)

        # Push the node on the stack of block commands.
        self.nested_nodes.append(node)

# ----------------------------------------------------------------------------------------------------------------------
