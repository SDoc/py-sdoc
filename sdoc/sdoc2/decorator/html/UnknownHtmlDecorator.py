"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ---------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlDecorator import HtmlDecorator

class UnknownHtmlDecorator(HtmlDecorator):
    """
    HtmlDecorator for generating HTML code for unknown nodes.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a unknown node.

        :param sdoc.sdoc2.node.UnknownNode.UnknownNode node: The unknown node.
        :param file file: The output file.
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('unknown', 'html', UnknownHtmlDecorator)