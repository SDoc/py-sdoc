from typing import Any, List, Optional

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TableNode import TableNode
from sdoc.sdoc2.NodeStore import NodeStore


class TableHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for table.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: TableNode, file: Any) -> None:
        """
        Generates the HTML code for a table node.

        :param TableNode node: The table node.
        :param any file: The output file.
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
    def _generate_caption(node: TableNode) -> str:
        """
        Generates the caption for the table in HTML representation.

        :param TableNode node: The table node.

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
    def _generate_table_body(node: TableNode) -> str:
        """
        Generates table with header.

        :param TableNode node: The table node.
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
    def _generate_table_cell(align: Optional[str], cell: Any) -> str:
        """
        Returns the 'column' with HTML data.

        :param str|None align:
        :param any cell: The column in a table.
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
    def _get_align(align_list: List[Optional[str]], column: int) -> Optional[List[Optional[str]]]:
        """
        Returns the align or None.

        :param list[str|None] align_list: The list with alignments.
        :param int column: The number of column.
        """
        if column in range(len(align_list)):
            return align_list[column]

        return None


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('table', 'html', TableHtmlFormatter)
