from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.SmileNode import SmileNode
from sdoc.sdoc2.NodeStore import NodeStore


class SmileHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for smile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: SmileNode, file: Any) -> None:
        """
        Generates the HTML code for a smile node.

        :param SmileNode node: The smile node.
        :param any file: The output file.
        """
        file.write(SmileHtmlFormatter.get_html())

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html() -> str:
        """
        Returns string with generated HTML tag for smile.

        :rtype: str
        """
        return Html.generate_element('b', {}, 'SMILE')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('smile', 'html', SmileHtmlFormatter)
