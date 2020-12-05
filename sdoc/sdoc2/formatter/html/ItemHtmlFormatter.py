from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ItemNode import ItemNode
from sdoc.sdoc2.NodeStore import NodeStore


class ItemHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: ItemNode, file: Any) -> None:
        """
        Generates the HTML code for an item node.

        :param ItemNode node: The item node.
        :param any file: The output file.
        """
        attributes = {'id': node.get_option_value('id')}

        file.write('<li {0}>'.format(Html.generate_attribute('id', attributes['id'])))
        node.prepare_content_tree()
        HtmlFormatter.generate(self, node, file)
        file.write('</li>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('item', 'html', ItemHtmlFormatter)
