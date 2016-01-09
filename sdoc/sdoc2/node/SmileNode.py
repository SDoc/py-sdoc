"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, CONTENT_TYPE_PHRASING
from sdoc.sdoc2.node.Node import Node


class SmileNode(Node):
    """
    SDoc2 node for development testing.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('smile')

    # ------------------------------------------------------------------------------------------------------------------
    def get_content_categories(self):
        """
        Returns the content types of this node.

        :rtype: set(int)
        """
        return {CONTENT_TYPE_PHRASING}

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
        Returns True.

        :rtype: bool
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('smile', SmileNode)
