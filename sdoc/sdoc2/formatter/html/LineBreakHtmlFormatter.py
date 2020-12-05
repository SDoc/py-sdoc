from typing import Any

from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.LineBreakNode import LineBreakNode
from sdoc.sdoc2.NodeStore import NodeStore


class LineBreakHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for a linebreak.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: LineBreakNode, file: Any) -> None:
        """
        Generates the HTML code for a smile node.

        :param LineBreakNode node: The linebreak node.
        :param any file: The output file.
        """
        file.write('<br/>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('br', 'html', LineBreakHtmlFormatter)
