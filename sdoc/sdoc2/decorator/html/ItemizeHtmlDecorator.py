"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlDecorator import HtmlDecorator


class ItemizeHtmlDecorator(HtmlDecorator):
    """
    HtmlDecorator for generating HTML code for itemize.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for an itemize node.

        :param sdoc.sdoc2.node.ItemizeNode.ItemizeNode node: The itemize node.
        :param file file: The output file.
        """
        file.write('<ul>')
        super().generate(node, file)
        file.write('</ul>')


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('itemize', 'html', ItemizeHtmlDecorator)
