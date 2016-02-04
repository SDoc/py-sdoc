"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class ParagraphNode(HeadingNode):
    """
    SDoc2 node for paragraphs.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('paragraph')

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
    def prepare_content_tree(self):
        """
        Not implemented for paragraph nodes.
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('paragraph', ParagraphNode)