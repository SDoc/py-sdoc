"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
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

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('TEXT', 'html', TextHtmlFormatter)
