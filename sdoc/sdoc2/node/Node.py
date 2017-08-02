"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc

from sdoc.sdoc2 import in_scope, out_scope, node_store


class Node(metaclass=abc.ABCMeta):
    """
    Abstract class for SDoc2 nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, name, options=None, argument=''):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param str name: The (command) name of this node.
        :param dict[str,str] options: The options of this node.
        :param str argument: The argument of this node (inline commands only).
        """
        self._io = io
        """
        The IO object.

        :type None|cleo.styles.output_style.OutputStyle:
        """

        self.id = 0
        """
        The ID of this SDoc2 node.

        :type: int
        """

        self.name = name
        """
        The (command) name of this node.

        :type: str
        """

        self._argument = argument
        """
        The argument of this node (inline commands only).

        :type: str
        """

        self._options = options if options else {}
        """
        The options of this node.

        :type: dict[str,mixed]
        """

        self.child_nodes = []
        """
        The ID's of the SDoc2 child nodes of this SDoc2 node.

        :type: list[int]
        """

        self.position = None
        """
        The position where this node is defined.

        :type: None|sdoc.sdoc2.Position.Position
        """

        self.labels = []
        """
        The list of labels in the node.

        :type:
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def io(self):
        """
        Getter for io.

        :rtype: cleo.styles.output_style.OutputStyle
        """
        return self._io

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def argument(self):
        """
        Getter for argument.

        :rtype: str
        """
        return self._argument

    # ------------------------------------------------------------------------------------------------------------------
    @argument.setter
    def argument(self, new_argument):
        """
        Setter for argument.

        :param str new_argument: The new argument.
        """
        self._argument = new_argument

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        self.io.writeln("{0!s}{1:4d} {2!s}".format(' ' * 4 * level, self.id, self.name))

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            node.print_info(level + 1)

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def _remove_child_nodes(self, node_list):
        """
        Removes child nodes from list of child nodes of this node.

        :param list[int] node_list: The child nodes the be removed.
        """
        for node in node_list:
            self.child_nodes.remove(node)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self):
        """
        Returns the hierarchy name if this node is a part of a hierarchy. Otherwise returns False.

        :rtype: str|bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def get_command(self):
        """
        Returns command of this node.

        :rtype: str
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns the hierarchy level if this node is a part of a hierarchy.

        :param int parent_hierarchy_level: The hierarchy level of the parent node in the same hierarchy.

        :rtype: int
        """
        raise RuntimeError("This method MUST only be called when a node is a part of an hierarchy.")

    # ------------------------------------------------------------------------------------------------------------------
    def get_option_value(self, option_name):
        """
        Returns the value of an option. Returns None if the option is not set.

        :param str option_name: The name of the option.

        :rtype: str|None
        """
        return self._options[option_name] if option_name in self._options else None

    # ------------------------------------------------------------------------------------------------------------------
    def set_option_value(self, option, value):
        """
        Sets value for option.

        :param str option: The name of an option
        :param str value: The value of an option
        """
        self._options[option] = value

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_block_command(self):
        """
        Returns True if this node is created by a block command. Otherwise returns False.

        :rtype: bool
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def is_document_root(self):
        """
        Returns True if this node is a document root node. Otherwise returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_hierarchy_root(self):
        """
        Returns True if this node can be the root of a hierarchy. Otherwise returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_inline_command(self):
        """
        Returns True if this node is created by a inline command. Otherwise returns False.

        :rtype: bool
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True if this node is a phrasing node, i.e. is a part of a paragraph. Otherwise returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_list_element(self):
        """
        Returns True if this node is a list element, e.g. an item in itemize. Otherwise returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def append_child_node(self, child_node):
        """
        Appends a child node to the list of child nodes of the node.

        :param sdoc.sdoc2.node.Node.Node child_node: The new child node
        """
        self.child_nodes.append(child_node.id)

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            node.prepare_content_tree()

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers):
        """
        Numbers all numerable nodes such as chapters, sections, figures, and, items.

        :param numbers: The current numbers.
        """
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            node.number(numbers)

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def get_enumerated_items(self):
        """
        Returns a list with a tuple with command and number of enumerated child nodes.

        This method is intended for unit test only.

        :rtype: list[(str,str)]
        """
        items = list()

        # First append the enumeration of this node (if any).
        if 'number' in self._options:
            items.append((self.get_command(), self._options['number'], self._argument))

        # Second append the enumeration of child nodes (if any).
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            tmp = node.get_enumerated_items()
            if tmp:
                items.append(tmp)

            out_scope(node)

        return items

    # ------------------------------------------------------------------------------------------------------------------
    def parse_labels(self):
        """
        Parses all labels and call methods to collect labels.
        """
        self.modify_label_list()

        if self.labels:
            self.set_id_heading_node()

    # ------------------------------------------------------------------------------------------------------------------
    def modify_label_list(self):
        """
        Creates label list for each heading node, and for node_store. Removes label nodes from child list.
        """
        obsolete_node_ids = []
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if node.get_command() == 'label':
                # Appending in Node labels list.
                self.labels.append(node.id)

                self.append_label_list_in_node_store(node)
                if self.get_option_value('number'):
                    label_arg = self.get_option_value('number')
                    title_attribute = self.argument
                else:
                    label_arg = self.argument
                    title_attribute = None

                node_store.labels[node.argument] = {'argument': label_arg,
                                                    'title':    title_attribute}

                # Removing node from child nodes.
                obsolete_node_ids.append(node.id)

            node.parse_labels()

            out_scope(node)

        self._remove_child_nodes(obsolete_node_ids)

    # ------------------------------------------------------------------------------------------------------------------
    def append_label_list_in_node_store(self, node):
        """
        Appending in NodeStore labels list.

        :param sdoc.sdoc2.node.Node.Node node: The current node.
        """
        if node.argument not in node_store.labels:
            if self.argument:
                node_store.labels[node.argument] = self.argument

            else:
                if 'number' in self._options:
                    node_store.labels[node.argument] = self._options['number']
                else:
                    node_store.labels[node.argument] = node.argument

        else:
            # @todo log definitions of both labels
            raise NameError('Duplicate label', node.argument)

    # ------------------------------------------------------------------------------------------------------------------
    def set_id_heading_node(self):
        """
        Sets id to heading node. (Argument of first label)
        """
        node = in_scope(self.labels[0])
        self._options['id'] = node.argument
        out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def change_ref_argument(self):
        """
        Changes reference argument on number of depending heading node.
        """
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if node.get_command() == 'ref':

                if node.argument in node_store.labels:
                    node.set_option_value('href', '#{0}'.format(node.argument))

                    if node_store.labels[node.argument]['title']:
                        node.set_option_value('title', node_store.labels[node.argument]['title'])

                    node.text = node_store.labels[node.argument]['argument']

                else:
                    node_store.error("Label '{}' not found".format(node.argument), node)

            node.change_ref_argument()

            out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
