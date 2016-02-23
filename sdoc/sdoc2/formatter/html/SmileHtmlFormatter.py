"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlFormatter import HtmlFormatter


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
        file.write(Html.generate_element('b', {}, 'SMILE'))

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('smile', 'html', SmileHtmlFormatter)
