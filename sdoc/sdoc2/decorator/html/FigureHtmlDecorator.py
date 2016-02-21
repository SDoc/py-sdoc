"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlDecorator import HtmlDecorator


class FigureHtmlDecorator(HtmlDecorator):
    """
    HtmlDecorator for generating HTML code for figures.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a figure node.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        text_in_tag = '%s %s' % (node._options['number'], '---FIGURE---')
        file.write(Html.generate_element('h3', {}, text_in_tag))

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('figure', 'html', FigureHtmlDecorator)
