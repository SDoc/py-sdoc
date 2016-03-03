"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc

from sdoc.sdoc2 import in_scope, out_scope


class Node:
    """
    Abstract class for SDoc2 nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name, options=None, argument=''):
        """
        Object constructor.

        :param str name: The (command) name of this node.
        :param dict[str,str] options: The options of this node.
        :param str argument: The argument of this node (inline commands only).
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

        :type: dict[str,int|str]
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

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def argument(self):
        """
        Getter for argument.

        :rtype: str
        """
        return self._argument

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        print("{0!s}{1:4d} {2!s}".format(' ' * 4 * level, self.id, self.name))
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            node.print_info(level + 1)

            out_scope(node)

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

        :rtype: str
        """
        return self._options[option_name] if option_name in self._options else None

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

        Thi method is intended for unit test only.

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

# ----------------------------------------------------------------------------------------------------------------------
