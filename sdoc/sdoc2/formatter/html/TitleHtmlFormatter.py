from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TitleNode import TitleNode
from sdoc.sdoc2.NodeStore import NodeStore


class TitleHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for title of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: TitleNode, file: Any) -> None:
        """
        Generates HTML code for a title node.

        :param TitleNode node: The title node.
        :param any file: The output file.
        """
        html_code = Html.generate_element('span', {}, node.argument)

        file.write(html_code)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('title', 'html', TitleHtmlFormatter)
