"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class ItemHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for items.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for an item node.

        :param sdoc.sdoc2.node.ItemNode.ItemNode node: The item node.
        :param file file: The output file.
        """
        file.write('<li>')
        node.prepare_content_tree()
        super().generate(node, file)
        file.write('</li>')


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('item', 'html', ItemHtmlFormatter)
