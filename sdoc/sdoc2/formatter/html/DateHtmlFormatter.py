from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.DateNode import DateNode
from sdoc.sdoc2.NodeStore import NodeStore


class DateHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for date of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: DateNode, file: Any) -> None:
        """
        Generates HTML code for a date node.

        :param DateNode node: The date node.
        :param any file: The output file.
        """
        html = Html.generate_element('span', {}, node.argument)

        file.write(html)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('date', 'html', DateHtmlFormatter)
