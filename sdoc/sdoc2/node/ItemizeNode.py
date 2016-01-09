"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2 import CONTENT_TYPE_FLOW, CONTENT_TYPE_PALPABLE
from sdoc.sdoc2.node.Node import Node


class ItemizeNode(Node):
    """
    SDoc2 node for itemize.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('itemize')

    # ------------------------------------------------------------------------------------------------------------------
    def get_content_categories(self):
        """
        Returns the content types of this node.

        :rtype: set(int)
        """
        return {CONTENT_TYPE_FLOW, CONTENT_TYPE_PALPABLE}

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('itemize', ItemizeNode)
