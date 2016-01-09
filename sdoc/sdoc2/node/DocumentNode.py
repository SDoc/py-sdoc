"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, CONTENT_TYPE_SECTION
from sdoc.sdoc2.node.Node import Node


class DocumentNode(Node):
    """
    SDoc2 node for documents.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('document')

    # ------------------------------------------------------------------------------------------------------------------
    def get_content_categories(self):
        """
        Returns the content types of this node.

        :rtype: set(int)
        """
        return {CONTENT_TYPE_SECTION}

    # ------------------------------------------------------------------------------------------------------------------
    def get_heading_level(self):
        return 0

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

    # ------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('document', DocumentNode)
