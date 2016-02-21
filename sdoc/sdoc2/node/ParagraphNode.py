"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class ParagraphNode(HeadingNode):
    """
    SDoc2 node for paragraphs.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: Not used.
        :param str argument: The text of this paragraph.
        """
        super().__init__('paragraph', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. paragraph.

        :rtype: str
        """
        return 'paragraph'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prune_whitespace(self):
        """
        Removes spaces from end of a paragraph.
        """
        first = self._child_nodes[0]
        last = self._child_nodes[-1]

        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                if node.id == first:
                    node.prune_whitespace(leading=True)
                if node.id == last:
                    node.prune_whitespace(trailing=True)
                if node.id != last and node.id != first:
                    node.prune_whitespace()

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('paragraph', ParagraphNode)
