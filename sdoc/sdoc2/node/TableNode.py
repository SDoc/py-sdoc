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

        self.table = []
        """
        The table with items.

        :type: list[list[str]]
        """

        self.table_header = []
        """
        The header of the table (If header is exists).

        :type: list[str]
        """

        self.table_aligns = []
        """
        The alignment for each column of the table (If header is exists).

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
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            self.create_table(node)

            node.prepare_content_tree()

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def create_table(self, node):
        """
        Splits text of a TextNode. Creates a table.

        :param sdoc.sdoc2.node.Node.Node node: The node which may be interpreted as table.
        """
        temp_table_items = node._argument.split('\n')

        # Remove empty elements.
        while '' in temp_table_items:
            temp_table_items.remove('')

        # Create a table.
        table = []
        for item in temp_table_items:
            string = io.StringIO(item)
            reader = csv.reader(string, delimiter='|')
            for line in reader:
                row = line
                table.append(row)

        if self.is_header_exist(table):
            self.table_header = table[0]
            self.table = table[2:]
            self.table_aligns = self.set_column_alignments(table[1])
        else:
            self.table = table

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def is_header_exist(header_array):
        """
        Checks if header is in the table.

        :param list[str] header_array: List with the data.

        :rtype: bool
        """
        is_header = True
        for align in header_array[1]:
            header_part = re.findall('[:]?[-]+[:]?', align)
            if not header_part:
                is_header = False
                break

        return is_header

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set_column_alignments(align_array):
        """
        Sets alignments on table columns.

        :param list[str|None] align_array: List of alignments.

        :rtype: list[str|None]
        """
        alignments = []
        for align in align_array:
            if align.strip().startswith(':') and align.strip().endswith(':'):
                alignments.append('center')
            elif align.strip().startswith(':'):
                alignments.append('left')
            elif align.strip().endswith(':'):
                alignments.append('right')
            else:
                alignments.append(None)

        return alignments

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('table', TableNode)
