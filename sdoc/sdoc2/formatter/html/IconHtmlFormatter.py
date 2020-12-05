from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.IconNode import IconNode
from sdoc.sdoc2.NodeStore import NodeStore


class IconHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for icons in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: IconNode, file: Any) -> None:
        """
        Generates the HTML code for an icon node.

        :param IconNode node: The icon node.
        :param any file: The output file.
        """
        attributes = IconNode.get_definition(node.argument)

        if attributes:
            img_element = Html.generate_void_element('img', attributes)
            file.write(img_element)
        else:
            NodeStore.error("There is no definition for icon with name '{}'".format(node.argument), node)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('icon', 'html', IconHtmlFormatter)
