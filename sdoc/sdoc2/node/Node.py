"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc

from sdoc.sdoc2 import node_store


class Node:
    """
    Abstract class for SDoc2 nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name, options=dict, argument=''):
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

        self._options = options
        """
        The options of this node.

        :type: dict[str,int|str]
        """

        self._child_nodes = []
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
    def print_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        print("%s%4d %s" % (' ' * 4 * level, self.id, self.name))
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            node.print_info(level + 1)

            node_store.out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self):
        """
        Returns the hierarchy name if this node is a part of a hierarchy. Otherwise returns False.

        :rtype: str|bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def get_enumerable_name(self):
        """
        Returns name of an enumerable node.

        :type: str|bool
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
    def append_child_node(self, child_node):
        """
        Appends a child node to the list of child nodes of the node.

        :param sdoc.sdoc2.node.Node.Node child_node: The new child node
        """
        self._child_nodes.append(child_node.id)

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            node.prepare_content_tree()

            node_store.out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            node.enumerate(numbers)

            node_store.out_scope(node)


# ----------------------------------------------------------------------------------------------------------------------
