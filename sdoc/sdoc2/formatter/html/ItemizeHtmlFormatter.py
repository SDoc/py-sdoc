from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class ItemizeHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for itemize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for an itemize node.

        :param sdoc.sdoc2.node.ItemizeNode.ItemizeNode node: The itemize node.
        :param file file: The output file.
        """
        file.write('<ul>')
        HtmlFormatter.generate(self, node, file)
        file.write('</ul>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('itemize', 'html', ItemizeHtmlFormatter)
