"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class TextHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for text.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a text node.

        :param sdoc.sdoc2.node.TextNode.TextNode node: The text node.
        :param file file: The output file.
        """
        file.write(Html.escape(node.argument))

        HtmlFormatter.generate(self, node, file)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('TEXT', 'html', TextHtmlFormatter)
