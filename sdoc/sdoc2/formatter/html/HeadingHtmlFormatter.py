"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class HeadingHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for headings.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        self.generate_heading_node(node, file)
        super().generate(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates HTML file structure if the node is chapter otherwise use method for generating heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        if node.get_command() == 'chapter':
            file_name = 'output_{0}.html'.format(node.argument)
            self._io.writeln('Writing <fso>{0!s}</fso>'.format(file_name))
            with open(file_name, 'wt', encoding='utf8') as file:
                file.write('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="NL" lang="NL">')
                file.write('<head><meta charset="UTF-8"/><title>sdoc</title></head>')
                file.write('<body>')

                self.generate_heading_node(node, file)
                super().generate_chapter(node, file)

                file.write('</body>')
                file.write('</html>')
        else:
            if file:
                self.generate_heading_node(node, file)
                super().generate_chapter(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_heading_node(node, file):
        """
        Generates the HTML code for heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        # Set id attribute to heading node.
        attributes = {'id': node.get_option_value('id')}

        number = node.get_option_value('number')
        text_in_tag = '{0} {1!s}'.format('' if not number else number, node.argument)
        file.write(Html.generate_element('h{0:d}'.format(node.get_hierarchy_level()), attributes, text_in_tag))

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('chapter', 'html', HeadingHtmlFormatter)
node_store.register_formatter('section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('subsection', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub2section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub3section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub4section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub5section', 'html', HeadingHtmlFormatter)
