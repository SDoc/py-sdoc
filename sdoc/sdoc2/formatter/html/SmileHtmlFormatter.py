"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class SmileHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for smile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a smile node.

        :param sdoc.sdoc2.node.SmileNode.SmileNode node: The smile node.
        :param file file: The output file.
        """
        file.write(SmileHtmlFormatter.get_html())

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html():
        """
        Returns string with generated HTML tag for smile.

        :rtype: str
        """
        return Html.generate_element('b', {}, 'SMILE')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('smile', 'html', SmileHtmlFormatter)
