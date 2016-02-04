"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""

# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store


class Node:
    """
    Abstract class for SDoc2 nodes.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name):
        """
        Object constructor.

        :param str name: The (command) name of this node.
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

        self.argument = ''
        """
        The argument of this node (inline commands only).

        :type: str
        """

        self.options = ''
        """
        The options of this node.

        :type: dict[str,int|str]
        """

        self.nodes = []
        """
        The ID's of the SDoc2 child nodes of this SDoc2 node.

        :type: list[int]
        """

        # @todo position of this node in source

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        print("%s%4d %s" % (' ' * 4*level, self.id, self.name))
        for node_id in self.nodes:
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
    def get_hierarchy_level(self):
        """
        Returns the hierarchy level if this node is a part of a hierarchy.

        :rtype: int
        """
        raise RuntimeError("This method MUST only be called when a node is a part of an hierarchy.")

    # ------------------------------------------------------------------------------------------------------------------
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
    def prepare_content_tree(self):
        """
        Prepares the content tree.
        """
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            node.prepare_content_tree()

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
