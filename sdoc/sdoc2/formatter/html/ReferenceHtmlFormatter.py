from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ReferenceNode import ReferenceNode
from sdoc.sdoc2.NodeStore import NodeStore


class ReferenceHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: ReferenceNode, file: Any) -> None:
        """
        Generates the HTML code for a reference node.

        :param ReferenceNode node: The reference node.
        :param any file: The output file.
        """
        self.write_into_file(node, file)

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_into_file(node: ReferenceNode, file: Any) -> None:
        """
        Writes data into opened file.

        :param ReferenceNode node: The reference node.
        :param any file: The output file.
        """
        file.write(ReferenceHtmlFormatter.get_html(node))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html(node: ReferenceNode) -> str:
        """
        Returns string with generated HTML tag.

        :param ReferenceNode node: The reference node.
        """
        attributes = {'class': node.get_option_value('class'),
                      'href':  node.get_option_value('href'),
                      'title': node.get_option_value('title')}

        return Html.generate_element('a', attributes, str(node.text))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('ref', 'html', ReferenceHtmlFormatter)
