from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.HyperlinkNode import HyperlinkNode
from sdoc.sdoc2.NodeStore import NodeStore


class HyperlinkHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for hyperlinks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: HyperlinkNode, file: Any) -> None:
        """
        Generates the HTML code for a hyperlink node.

        :param HyperlinkNode node: The hyperlink node.
        :param any file: The output file.
        """
        file.write(HyperlinkHtmlFormatter.get_html(node))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html(node: HyperlinkNode) -> str:
        """
        Returns string with generated HTML tag.

        :param HyperlinkNode node: The hyperlink node.
        """
        return Html.generate_element('a', node.get_html_attributes(), node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('hyperlink', 'html', HyperlinkHtmlFormatter)
