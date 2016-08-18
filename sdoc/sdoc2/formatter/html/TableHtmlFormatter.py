"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ReferenceNode import ReferenceNode


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
        self.write_into_file(node, file)

    # ------------------------------------------------------------------------------------------------------------------
    def write_into_file(self, node, file):
        """
        Writes data into opened file.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.
        :param file file: The output file.
        """
        # Attributes for table.
        table_attrs = {'class': node.get_option_value('class')}

        if node.column_headers:
            rows = self.generate_table_with_header(node)
        else:
            rows = self.generate_table(node)

        html_table = Html.generate_element('table', table_attrs, rows, True)

        file.write(html_table)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_table(node):
        """
        Generates table without header.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.

        :rtype: str
        """
        columns = ''
        rows = ''

        for row in node.rows:
            for column in row:
                columns += Html.generate_element('td', {}, column)
            rows += Html.generate_element('tr', {}, columns, True)
            columns = ''

        return rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_table_with_header(node):
        """
        Generates table with header.

        :param sdoc.sdoc2.node.TableNode.TableNode node: The table node.

        :rtype: str
        """
        table_header = ''
        columns = ''
        rows = ''

        for column in node.column_headers:
            table_header += Html.generate_element('th', {}, column, True)
        table_header = Html.generate_element('tr', {}, table_header, True)

        header_column_counter = 0

        for row in node.rows:
            for col in row:
                align = TableHtmlFormatter.get_align(node.alignments, header_column_counter)

                columns += TableHtmlFormatter.generate_column(align, col)

                header_column_counter += 1
            rows += Html.generate_element('tr', {}, columns, True)
            columns = ''
            header_column_counter = 0

        return table_header + rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_column(align, col):
        """
        Returns the 'column' with HTML data.

        :param mixed col: The column in a table.

        :rtype: str
        """
        if isinstance(col, str):
            if align:
                column = Html.generate_element('td', {'style': "text-align: {0}".format(align)}, col)
            else:
                column = Html.generate_element('td', {}, col)

        else:
            # Generates html in nested node ('col') with specified formatter.
            formatter = node_store.get_formatter('html', col.get_command())
            node_html = formatter.get_html(col)

            if align:
                column = Html.generate_element('td',
                                               {'style': "text-align: {0}".format(align)},
                                               node_html,
                                               is_html=True)
            else:
                column = Html.generate_element('td', {}, node_html, is_html=True)

        return column

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_align(align_list, column):
        """
        Returns the align or None.

        :param list[str|None] align_list: The list with alignments.
        :param int column: The number of column.

        :rtype: list[str|None] | None
        """
        try:
            return align_list[column]
        except IndexError:
            return None


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('table', 'html', TableHtmlFormatter)
