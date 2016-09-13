"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class ParagraphNode(HeadingNode):
    """
    SDoc2 node for paragraphs.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: Not used.
        :param str argument: The text of this paragraph.
        """
        super().__init__(io, 'paragraph', options, argument)

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
    def number(self, numbers):
        """
        Overrides the HeadingNode implementation with the (original) Node implementation.

        :param dict[str,str] numbers: The number of last node.
        """
        Node.number(self, numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def set_toc_id(self):
        """
        Don't do anything. Because we needn't this behaviour here.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def prune_whitespace(self):
        """
        Removes spaces from end of a paragraph.
        """
        first = self.child_nodes[0]
        last = self.child_nodes[-1]

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                if node.id == first:
                    node.prune_whitespace(leading=True)
                if node.id == last:
                    node.prune_whitespace(trailing=True)
                if node.id != last and node.id != first:
                    node.prune_whitespace()

            out_scope(node)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('paragraph', ParagraphNode)
