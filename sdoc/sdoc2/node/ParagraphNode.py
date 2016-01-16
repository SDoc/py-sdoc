"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.node.Node import Node


class ParagraphNode(Node):
    """
    SDoc2 node for paragraphs.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('paragraph')

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level):
        """
        Temp function for development
        :param level: the level of block commands.
        """

        print("%s%4d %s %s" % (' ' * 4 * level, self.id, self.name, self.argument))

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False


# ----------------------------------------------------------------------------------------------------------------------
