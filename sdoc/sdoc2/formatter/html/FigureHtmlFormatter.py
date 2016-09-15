"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
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

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _write_caption(node, file):
        """
        Generates the caption for the table in HTML representation.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        if node.caption:
            figure_number = node.get_option_value('number')

            if figure_number:
                inner_text = 'Figuur {}: {}'.format(figure_number, node.caption)  # TODO Internationalization
            else:
                inner_text = node.caption

            file.write(Html.generate_element('figcaption', {}, inner_text))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_into_file(node, file):
        """
        Writes data into opened HTML file.

        :param sdoc.sdoc2.node.FigureNode.FigureNode node: The figure node.
        :param file file: The output file.
        """
        # Creating dicts with attributes for each type of element.
        figure_attributes = {'id': node.get_option_value('id')}

        img_attributes = {'src':    node.get_option_value('src'),
                          'width':  node.get_option_value('width'),
                          'height': node.get_option_value('height'),
                          'alt':    node.caption}

        # Creating elements.
        file.write(Html.generate_tag('figure', figure_attributes))

        file.write(Html.generate_void_element('img', img_attributes))

        FigureHtmlFormatter._write_caption(node, file)

        file.write('</figure>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('figure', 'html', FigureHtmlFormatter)
