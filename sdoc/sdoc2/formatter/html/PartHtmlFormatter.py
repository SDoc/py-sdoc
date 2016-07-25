"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import os

from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class PartHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for parts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a part node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        if os.path.exists('output.html'):
            os.remove('output.html')

        file_name = 'output_{0}.html'.format(node.argument)
        self._io.writeln('Writing <fso>{0!s}</fso>'.format(file_name))

        with open(file_name, 'w') as file:
            file.write('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="NL" lang="NL">')
            file.write('<head><meta charset="UTF-8"/><title>sdoc</title></head>')
            file.write('<body>')

            self.generate_part_node(node, file)
            super().generate(node, file)

            file.write('</body>')
            file.write('</html>')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_part_node(node, file):
        """
        Generates the HTML code for part node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        # Set id attribute to heading node.
        attributes = {'id': node.get_option_value('id'), 'class': 'part'}

        number = node.get_option_value('number')
        text_in_tag = '{0} {1!s}'.format('' if not number else number, node.argument)
        file.write(Html.generate_element('div', attributes, text_in_tag))

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('part', 'html', PartHtmlFormatter)
