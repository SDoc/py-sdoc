"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class TocHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for table of contents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a table of contents node.

        :param sdoc.sdoc2.node.TocNode.TocNode node: The table of contents node.
        :param file file: The output file.
        """
        self.write_into_file(node, file)

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_into_file(node, file):
        """
        Writes data into opened file.

        :param sdoc.sdoc2.node.TocNode.TocNode node: The table of contents node.
        :param file file: The output file.
        """
        attributes = {'role': 'navigation', 'class': 'table-of-contents'}

        file.write(Html.generate_tag('nav', attributes))
        file.write(Html.generate_element('h3', {}, node.argument))

        file.write('<ul>')
        TocHtmlFormatter.write_contents(node, file)
        file.write('</ul>')

        file.write('</nav>')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_contents(node, file):
        """
        Writes the contents into file.

        :param sdoc.sdoc2.node.TocNode.TocNode node: The table of contents node.
        :param file file: The output file.
        """
        depth = node.get_option_value('depth')

        for item in node.get_option_value('ids'):
            if depth and item['level'] <= int(depth):
                TocHtmlFormatter.write_elements(item, file)

            elif not depth:
                TocHtmlFormatter.write_elements(item, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def write_elements(item, file):
        """
        Write the containing elements.

        :param dict[str,str] item: The item which we outputs.
        :param file file: The output file.
        """
        class_attr = 'level{}'.format(item['level'])
        file.write(Html.generate_tag('li', {'class': class_attr}))

        file.write(Html.generate_tag('a', {'href': '#{}'.format(item['id'])}))

        number = item['number'] if item['numbering'] else None
        if number:
            file.write(Html.generate_element('span', {}, str(number)))

        file.write(' {}'.format(item['arg']))
        file.write('</a>')
        file.write('</li>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('toc', 'html', TocHtmlFormatter)
