"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
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

        super().generate(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates the HTML code for a reference node.

        :param sdoc.sdoc2.node.ReferenceNode.ReferenceNode node: The reference node.
        :param file file: The output file.
        """
        if file:
            self.write_into_file(node, file)

        super().generate_chapter(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_into_file(node, file):
        """
        Writes data into opened file.

        :param sdoc.sdoc2.node.ReferenceNode.ReferenceNode node: The reference node.
        :param file file: The output file.
        """
        attributes = {'class': node.get_option_value('class'),
                      'href': node.get_option_value('href')}

        file.write(Html.generate_element('a', attributes, node.argument))


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('ref', 'html', ReferenceHtmlFormatter)
