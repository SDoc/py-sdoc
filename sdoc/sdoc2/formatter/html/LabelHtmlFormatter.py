from typing import Any

from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.LabelNode import LabelNode
from sdoc.sdoc2.NodeStore import NodeStore


class LabelHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for labels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: LabelNode, file: Any) -> None:
        """
        Generates the HTML code for a label node.

        :param LabelNode node: The label node.
        :param any file: The output file.
        """
        HtmlFormatter.generate(self, node, file)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('label', 'html', LabelHtmlFormatter)
