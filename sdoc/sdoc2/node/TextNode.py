"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


class TextNode(Node):
    """
    SDoc2 node for items.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('TEXT')

    # ------------------------------------------------------------------------------------------------------------------
    def xprint_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        print("%s%4d %s %s" % (' ' * 4*level, self.id, self.name, self.argument))

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

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True.

        :rtype: bool
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('TEXT', TextNode)
