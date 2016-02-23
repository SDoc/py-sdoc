"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlFormatter import HtmlFormatter


class ParagraphHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for paragraph.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a paragraph node.

        :param sdoc.sdoc2.node.ParagraphNode.ParagraphNode node: The paragraph node.
        :param file file: The output file.
        """
        file.write('<p>')
        super().generate(node, file)
        file.write('</p>')


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('paragraph', 'html', ParagraphHtmlFormatter)
