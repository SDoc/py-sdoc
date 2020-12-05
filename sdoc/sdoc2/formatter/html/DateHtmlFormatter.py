from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class DateHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for date of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates HTML code for a date node.

        :param sdoc.sdoc2.node.DateNode.DateNode node: The date node.
        :param file file: The output file.
        """
        html = Html.generate_element('span', {}, node.argument)

        file.write(html)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('date', 'html', DateHtmlFormatter)
