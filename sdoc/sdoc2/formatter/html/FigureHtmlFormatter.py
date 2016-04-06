"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class FigureHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for figures.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a figure node.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        self.write_into_file(node, file)

        super().generate(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates the HTML code for a figure node.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        if file:
            self.write_into_file(node, file)

        super().generate_chapter(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    def write_into_file(self, node, file):
        """
        Writes data into opened HTML file.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        # Creating dicts with attributes for each type of element.
        img_attributes = {'src': node.get_option_value('filename'),
                          'width': node.get_option_value('width'),
                          'height': node.get_option_value('height'),
                          'alt': node.get_option_value('caption')}
        div_attributes = {'class': node.get_option_value('class')}

        # Creating elements.
        img_element = Html.generate_void_element('img', img_attributes)
        div_img_element = Html.generate_element('div', div_attributes, img_element, True)

        # Write elements into html file.
        file.write(div_img_element)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('figure', 'html', FigureHtmlFormatter)
