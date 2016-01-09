"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import CONTENT_TYPE_FLOW, CONTENT_TYPE_PALPABLE
from sdoc.sdoc2.node.Node import Node


class ParagraphNode(Node):
    """
    SDoc2 node for paragraphs.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('paragraph')

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
