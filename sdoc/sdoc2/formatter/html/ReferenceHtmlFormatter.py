"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class ReferenceHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a reference node.

        :param sdoc.sdoc2.node.ReferenceNode.ReferenceNode node: The reference node.
        :param file file: The output file.
        """
        self.write_into_file(node, file)

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_into_file(node, file):
        """
        Writes data into opened file.

        :param sdoc.sdoc2.node.ReferenceNode.ReferenceNode node: The reference node.
        :param file file: The output file.
        """
        file.write(ReferenceHtmlFormatter.get_html(node))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_html(node):
        """
        Returns string with generated HTML tag.

        :param sdoc.sdoc2.node.ReferenceNode.ReferenceNode node: The reference node.

        :rtype: str
        """
        attributes = {'class': node.get_option_value('class'),
                      'href':  node.get_option_value('href'),
                      'title': node.get_option_value('title')}

        return Html.generate_element('a', attributes, str(node.text))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('ref', 'html', ReferenceHtmlFormatter)
