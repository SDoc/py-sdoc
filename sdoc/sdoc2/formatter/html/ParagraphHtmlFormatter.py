"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


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
        HtmlFormatter.generate(self, node, file)
        file.write('</p>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('paragraph', 'html', ParagraphHtmlFormatter)
