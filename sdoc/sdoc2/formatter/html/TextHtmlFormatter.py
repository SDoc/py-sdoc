from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.NodeStore import NodeStore


class TextHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for text.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: TextNode, file: Any) -> None:
        """
        Generates the HTML code for a text node.

        :param TextNode node: The text node.
        :param any file: The output file.
        """
        file.write(Html.escape(node.argument))

        HtmlFormatter.generate(self, node, file)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('TEXT', 'html', TextHtmlFormatter)
