import csv
import io
import re
from typing import Any, Dict, List, Optional

from cleo.io.io import IO

from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.helper.Enumerable import Enumerable
from sdoc.sdoc2.node.CaptionNode import CaptionNode
from sdoc.sdoc2.node.LabelNode import LabelNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class TableNode(Node):
    """
    SDoc2 node for table.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io_object: IO, options: Dict[str, str]):
        """
        Object constructor.

        :param OutputStyle io_object: The IO object.
        :param dict[str,str] options: The options of this table.
        """
        super().__init__(io_object, 'table', options)

        self.rows: List[List[str]] = []
        """
        The table rows.
        """

        self.column_headers: List[str] = []
        """
        The column headers of the table (if any).
        """

        self.alignments: List[Optional[str]] = []
        """
        The text alignments in the table columns.
        """

        self.caption: Optional[str] = None
        """
        The caption for the table.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. table.
        """
        return 'table'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers: Dict[str, Any]) -> None:
        """
        Numbers all numerable nodes such as chapters, sections, figures, and, items.

        :param dict[str,any] numbers: The current numbers.
        """
        if 'table' not in numbers:
            numbers['table'] = Enumerable()
            numbers['table'].generate_numeration(1)
            numbers['table'].increment_last_level()
        else:
            numbers['table'].increment_last_level()

        self._options['number'] = numbers['table'].get_string()

        super().number(numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Prepares this node for further processing.
        """
        table_nodes = []

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, LabelNode):
                self.setup_label(node)

            elif isinstance(node, CaptionNode):
                self.caption = node.argument

            else:
                table_nodes.append(node)

            node.prepare_content_tree()

            out_scope(node)

        self.generate_table(table_nodes)

    # ------------------------------------------------------------------------------------------------------------------
    def setup_label(self, node):
        """
        Sets the data of a label to current table.

        :param sdoc.sdoc2.node.LabelNode.LabelNode node: The label node.
        """
        self._options['id'] = node.argument

    # ------------------------------------------------------------------------------------------------------------------
    def generate_table(self, nodes):
        """
        Generates the table node.

        :param list[sdoc.sdoc2.node.Node.Node] nodes: The list with nodes.
        """
        table_data = TableNode.divide_text_nodes(nodes)
        split_data = TableNode.split_by_new_lines(table_data)
        rows = self.generate_output_rows(split_data)

        if self.has_header(rows):
            self.column_headers = rows[0]
            self.rows = rows[2:]
            self.alignments = self.get_column_alignments(rows[1])
        else:
            self.rows = rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def divide_text_nodes(nodes: List[Any]) -> List[Any]:
        """
        Divides text nodes from other type of nodes.

        :param: list[any] nodes: The list with nodes.

        :rtype: list[any]
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
    def split_by_new_lines(table_data: List[Any]) -> List[Any]:
        """
        Splits data by newline symbols.

        :param list[any] table_data:

        :rtype: list[any]
        """
        split_data = []

        for data in table_data:
            if isinstance(data, str):
                split_data.append(data.split('\n'))
            else:
                split_data.append(data)

        for data in split_data:
            if isinstance(data, list):
                for element in data:
                    if element.isspace() or element == '':
                        data.remove(element)

        return split_data

    # ------------------------------------------------------------------------------------------------------------------
    def generate_output_rows(self, split_data: List[Any]) -> List[List[Any]]:
        """
        Generates the rows for final representation.

        :param list[any] split_data: The split data.

        :rtype: list[list[any]]
        """
        separated_data = TableNode.split_by_vertical_separators(split_data)

        rows = []

        for item in separated_data:
            row = []

            for data in item:
                if data and isinstance(data, str) and not data.isspace():
                    string = io.StringIO(data)
                    self.parse_vertical_separators(string, row)

                else:
                    if data:
                        row.append(data)

            if row:
                rows.append(row)

        return rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def split_by_vertical_separators(split_data: List[Any]) -> List[List[Any]]:
        """
        Splits data by vertical separators and creates rows with data.

        :param list[any] split_data: The split data.

        :rtype: list[list[any]]
        """
        rows = []
        row = []

        for item in split_data:
            # If we have a list we pass for each element.
            # In list we have only text elements.
            if isinstance(item, list):
                for element in item:

                    # If element starts with '|' we just add element to row.
                    if element.strip().startswith('|'):
                        row.append(element)

                    # If element ends with '|' we add row to rows list, reset row to empty list
                    # and append there current element. We do it because we know that if string ends with '|',
                    # after it we have non-text element.
                    elif element.strip().endswith('|'):
                        row = TableNode.reset_data(row, rows)
                        row.append(element)

                    # If we have element which not starts and not ends in '|' we do this block.
                    else:
                        # If last added element of row is not string we add row to rows list, reset row to empty.
                        if row and not isinstance(row[-1], str):
                            row = TableNode.reset_data(row, rows)
                        # And just add full element with text like a row to list of rows.
                        rows.append([element])

            # Do this block if element is not a list.
            else:
                # If last added element not ends with '|' we add row to rows list, and reset row to empty list.
                if row and not row[-1].strip().endswith('|'):
                    row = TableNode.reset_data(row, rows)
                # Add item to row.
                row.append(item)

        return rows

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def reset_data(row: List[Any], rows: List[List[any]]) -> List[Any]:
        """
        Appends row with data to list of rows, and clear row from any elements.

        Warning! This method changes original list 'rows'.

        :param list[any] row: The row with elements
        :param list[list[any]] rows: The list with many rows.
        """
        rows.append(row)
        return []

    # ------------------------------------------------------------------------------------------------------------------
    def parse_vertical_separators(self, string: io.StringIO, row: List[any]) -> None:
        """
        Splits row by vertical separator for future output.

        :param StringIO string: The string which we will separate.
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
    def has_header(rows: List[str]) -> bool:
        """
        Returns True if the table has a table header.

        :param list[str] rows: The second row of the table.
        """
        is_header = True

        if len(rows) == 1:
            return False

        for align in rows[1]:
            header_part = re.findall(':?---+-*:?', align)
            if not header_part:
                is_header = False
                break

        return is_header

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_column_alignments(row: List[str]) -> List[str]:
        """
        Sets alignments on table columns.

        :param list[str] row: The row with hyphens for creating column headers.
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
    def prune_whitespace(row: List[str]) -> List[str]:
        """
        Strips whitespaces from the text of an each cell.

        :param list[str] row: The row with text of an each cell.
        """
        clear_row = []
        for item in row:
            clear_text = item.strip()
            clear_text = re.sub(r'\s+', ' ', clear_text)
            clear_row.append(clear_text)

        return clear_row


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_block_command('table', TableNode)
