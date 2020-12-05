from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class LabelHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for labels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a label node.

        :param sdoc.sdoc2.node.LabelNode.LabelNode node: The label node.
        :param file file: The output file.
        """
        HtmlFormatter.generate(self, node, file)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('label', 'html', LabelHtmlFormatter)
