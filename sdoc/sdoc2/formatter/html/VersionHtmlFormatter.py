from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.VersionNode import VersionNode
from sdoc.sdoc2.NodeStore import NodeStore


class VersionHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for version of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: VersionNode, file: Any) -> None:
        """
        Generates HTML code for a version node.

        :param VersionNode node: The version node.
        :param any file: The output file.
        """
        html_code = Html.generate_element('span', {}, node.argument)

        file.write(html_code)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('version', 'html', VersionHtmlFormatter)
