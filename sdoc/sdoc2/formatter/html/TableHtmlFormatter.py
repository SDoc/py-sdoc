"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class TableHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for table.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a table node.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.
        :param file file: The output file.
        """
        attributes = {'class': node.get_option_value('class'),
                      'id':    node.get_option_value('id')}

        html = Html.generate_tag('table', attributes)

        html += TableHtmlFormatter._generate_caption(node)

        html += self._generate_table_body(node)

        html += '</table>'

        file.write(html)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _generate_caption(node):
        """
        Generates the caption for the table in HTML representation.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.

        :rtype: str
        """
        if node.caption:
            table_number = node.get_option_value('number')

            if table_number:
                inner_text = 'Tabel {}: {}'.format(table_number, node.caption)  # TODO Internationalization
            else:
                inner_text = node.caption

            return Html.generate_element('caption', {}, inner_text)

        return ''

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _generate_table_body(node):
        """
        Generates table with header.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.

        :rtype: str
        """
        html = '<tbody>'

        if node.column_headers:
            html += '<tr>'
            for column in node.column_headers:
                html += Html.generate_element('th', {}, column)
            html += '</tr>'

        for row in node.rows:
            header_column_counter = 0
            html += '<tr>'
            for col in row:
                align = TableHtmlFormatter._get_align(node.alignments, header_column_counter)
                html += TableHtmlFormatter._generate_table_cell(align, col)
                header_column_counter += 1
            html += '</tr>'

        html += '</tbody>'

        return html

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _generate_table_cell(align, cell):
        """
        Returns the 'column' with HTML data.

        :param mixed cell: The column in a table.

        :rtype: str
        """
        attributes = {}

        if align:
            attributes['style'] = "text-align: {0}".format(align)

        if isinstance(cell, str):
            data = cell
            is_html = False
        else:
            # Generates html in nested node ('cell') with specified formatter.
            formatter = NodeStore.get_formatter('html', cell.get_command())
            data = formatter.get_html(cell)
            is_html = True

        return Html.generate_element('td', attributes, data, is_html)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _get_align(align_list, column):
        """
        Returns the align or None.

        :param list[str|None] align_list: The list with alignments.
        :param int column: The number of column.

        :rtype: list[str|None] | None
        """
        if column in range(len(align_list)):
            return align_list[column]

        return None


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('table', 'html', TableHtmlFormatter)
