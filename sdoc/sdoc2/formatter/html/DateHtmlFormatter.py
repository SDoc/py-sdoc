"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


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
        text = 'Date: {}'.format(node.argument)
        html_code = Html.generate_element('h3', {}, text)

        file.write(html_code)

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('date', 'html', DateHtmlFormatter)
