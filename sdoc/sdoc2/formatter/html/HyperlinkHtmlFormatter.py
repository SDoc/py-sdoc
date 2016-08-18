"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class HyperlinkHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for hyperlinks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a hyperlink node.

        :param sdoc.sdoc2.node.HyperlinkNode.HyperlinkNode node: The hyperlink node.
        :param file file: The output file.
        """
        file.write(HyperlinkHtmlFormatter.get_html(node))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html(node):
        """
        Returns string with generated HTML tag.

        :param sdoc.sdoc2.node.HyperlinkNode.HyperlinkNode node: The hyperlink node.

        :rtype: str
        """
        return Html.generate_element('a', node.get_html_attributes(), node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('hyperlink', 'html', HyperlinkHtmlFormatter)
