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
    def get_content_categories(self):
        """
        Returns the content types of this node.

        :rtype: set(int)
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns True if this node is create by a block command.

        :rtype: bool
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True if this node is create by a inline command.

        :rtype: bool
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
