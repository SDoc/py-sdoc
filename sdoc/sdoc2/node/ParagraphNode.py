"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.TextNode import TextNode


class ParagraphNode(HeadingNode):
    """
    SDoc2 node for paragraphs.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('paragraph')

    # ------------------------------------------------------------------------------------------------------------------
    def gen_html(self, level, file):
        """
        Function for generating part of the HTML document.

        :param int level: the level of node.
        :param file file: the file where we write html.
        """
        file.write("<p>")
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            node.gen_html(level, file)

            node_store.out_scope(node)

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
        Removes spaces from end of a paragraph.
        """
        first = self.nodes[0]
        last = self.nodes[-1]

        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                if node.id == first:
                    node.prune_whitespace(leading=True)
                elif node.id == last:
                    node.prune_whitespace(trailing=True)
                else:
                    node.prune_whitespace()

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('paragraph', ParagraphNode)
