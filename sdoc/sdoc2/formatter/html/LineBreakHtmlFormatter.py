from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class LineBreakHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for a linebreak.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a smile node.

        :param sdoc.sdoc2.node.LineBreakNode.LineBreakNode node: The linebreak node.
        :param file file: The output file.
        """
        file.write('<br/>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('br', 'html', LineBreakHtmlFormatter)
