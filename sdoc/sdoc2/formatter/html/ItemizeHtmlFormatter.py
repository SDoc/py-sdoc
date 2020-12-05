from typing import Any

from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ItemizeNode import ItemizeNode
from sdoc.sdoc2.NodeStore import NodeStore


class ItemizeHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for itemize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: ItemizeNode, file: Any) -> None:
        """
        Generates the HTML code for an itemize node.

        :param ItemizeNode node: The itemize node.
        :param any file: The output file.
        """
        file.write('<ul>')
        HtmlFormatter.generate(self, node, file)
        file.write('</ul>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('itemize', 'html', ItemizeHtmlFormatter)
