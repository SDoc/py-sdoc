"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class TitleHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for title of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates HTML code for a title node.

        :param sdoc.sdoc2.node.TitleNode.TitleNode node: The title node.
        :param file file: The output file.
        """
        html_code = Html.generate_element('span', {}, node.argument)

        file.write(html_code)

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('title', 'html', TitleHtmlFormatter)
