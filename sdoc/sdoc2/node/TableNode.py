"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import re
import csv
import io
from sdoc.sdoc2 import node_store, in_scope, out_scope
from sdoc.sdoc2.node.Node import Node


class TableNode(Node):
    """
    SDoc2 node for table.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options):
        """
        Object constructor.

        :param dict[str,str] options: The options of this table.
        """
        super().__init__('table', options)

        self.rows = []
        """
        The table rows.

        :type: list[list[str]]
        """

        self.column_headers = []
        """
        The column headers of the table (if any).

        :type: list[str]
        """

        self.alignments = []
        """
        The text alignments in the table columns.

        :type: list[str|None]
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. table.

        :rtype: str
        """
        return 'table'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        table_nodes = []

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            table_nodes.append(node)
            node.prepare_content_tree()

            out_scope(node)

        self.extract_table(table_nodes)

    # ------------------------------------------------------------------------------------------------------------------
    def extract_table(self, nodes):
        """
        Extract the table data from a TextNode.

        :param list[sdoc.sdoc2.node.Node.Node] nodes: The list with nodes.
        """
        table_data = TableNode.separate_text_nodes(nodes)

        splitted_data = TableNode.split_by_rows(table_data)

        rows = self.derive_table_data(splitted_data)

        if self.has_header(rows):
            self.column_headers = rows[0]
            self.rows = rows[2:]
            self.alignments = self.get_column_alignments(rows[1])
        else:
            self.rows = rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def separate_text_nodes(nodes):
        """
        Separates text nodes from other type of nodes.

        :param: list[mixed] nodes: The list with nodes.

        :rtype: list[mixed]
        """
        table_data = []
        table_text_repr = ''

        for node in nodes:
            if node.get_command() == 'TEXT':
                table_text_repr += node.argument
            else:
                table_data.append(table_text_repr)
                table_data.append(node)
                table_text_repr = ''

        if table_text_repr:
            table_data.append(table_text_repr)

        return table_data

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def split_by_rows(table_data):
        """
        Splits data by rows.

        :param list[mixed] table_data:

        :rtype: list[mixed]
        """
        splitted_data = []

        for data in table_data:
            if type(data) == str:
                splitted_data.append(data.split('\n'))
            else:
                splitted_data.append(data)

        for data in splitted_data:
            if type(data) == list:
                for element in data:
                    if element.isspace() or element == '':
                        print('yeah!')
                        data.remove(element)

        for data in splitted_data:
            print(data)

        print()
        print()

        return splitted_data

    # ------------------------------------------------------------------------------------------------------------------
    def derive_table_data(self, splitted_data):
        """
        Generates table data.

        :param list[mixed] splitted_data: The splitted data.

        :rtype: list[list[mixed]]
        """
        separated_data = TableNode.split_by_vertical_separators(splitted_data)

        rows = []

        for item in separated_data:
            row = []

            for data in item:
                if type(data) == str:
                    string = io.StringIO(data)
                    self.parse_vertical_separators(string, row)
                else:
                    row.append(data)

            rows.append(row)

        return rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def split_by_vertical_separators(splitted_data):
        """
        Splits data by vertical separators and creates rows with data.

        :param list[mixed] splitted_data: The splitted data.

        :rtype: list[list[mixed]]
        """
        # for item in splitted_data:
        #     print(item)
        #
        # print()
        # print()

        rows = []
        row = []

        for item in splitted_data:
            if type(item) == list:

                for element in item:
                    if element.strip().startswith('|'):
                        row.append(element)

                    elif element.strip().endswith('|'):
                        if row and type(row[-1]) != str:
                            rows.append(row)
                            row = []
                        row.append(element)

                    else:
                        if row and type(row[-1]) != str:
                            rows.append(row)
                            row = []
                        rows.append([element])
            else:
                row.append(item)

        # print(rows)
        # print()
        # print()
        return rows

    # ------------------------------------------------------------------------------------------------------------------
    def parse_vertical_separators(self, string, row):
        """
        Splits row by vertical separator for future output.

        :param str string: The string which we will separate.
        :param list[mixed] row: The list with the row in which we append data.
        """
        reader = csv.reader(string, delimiter='|')
        for line in reader:
            new_row = self.prune_whitespace(line)

            for item in new_row:
                if item:
                    row.append(item)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def has_header(row):
        """
        Returns True if the table has a table header.

        :param list[str] row: The second row of the table.

        :rtype: bool
        """
        is_header = True

        if len(row) == 1:
            return False

        for align in row[1]:
            header_part = re.findall(':?---+-*:?', align)
            if not header_part:
                is_header = False
                break

        return is_header

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_column_alignments(row):
        """
        Sets alignments on table columns.

        :param list[str] row: The row with hyphens for creating column headers.

        :rtype: list[str]
        """
        alignments = []
        for hyphens in row:
            hyphens = hyphens.strip()
            if hyphens.startswith(':') and hyphens.endswith(':'):
                alignments.append('center')
            elif hyphens.startswith(':'):
                alignments.append('left')
            elif hyphens.endswith(':'):
                alignments.append('right')
            else:
                alignments.append('')

        return alignments

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def prune_whitespace(row):
        """
        Strips whitespaces from the text of an each cell.

        :param list[str] row: The row with text of an each cell.
        :rtype: list[str]
        """
        clear_row = []
        for item in row:
            clear_text = item.strip()
            clear_text = re.sub(r'\s+', ' ', clear_text)
            clear_row.append(clear_text)

        return clear_row

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('table', TableNode)
