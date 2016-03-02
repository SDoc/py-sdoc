import os
import ast
import csv
import unittest

import sdoc
from sdoc.sdoc2.SDoc2Interpreter import SDoc2Interpreter


class SDoc2EnumerationTest(unittest.TestCase):
    """
    Test cases for SDoc2 enumerations.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_list_of_items(self, nodes):
        """
        Takes a list of lists/tuples, converts to string, removes extra nesting and creates a tuple.

        :param list nodes: The list of nested lists/tuples of items.

        :rtype: tuple[tuple]
        """
        items_string = str(nodes)
        items_string = items_string.replace('[', '')
        items_string = items_string.replace(']', '')

        return ast.literal_eval(items_string)

    # ------------------------------------------------------------------------------------------------------------------
    def csv_to_tuple(self, file_name):
        """
        Reads a csv file, creates a tuple of csv objects.

        :param str file_name: The path to file.

        :rtype: tuple[tuple]
        """
        list_for_items = []

        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                list_for_items.append(tuple(row))

        items_tuple = tuple(list_for_items)

        return items_tuple

    # ------------------------------------------------------------------------------------------------------------------
    def run_test(self, sdoc_name):
        data_dir = os.path.dirname(os.path.abspath(__file__)) + '/enumeration/'

        pre, ext = os.path.splitext(sdoc_name)
        file_name = data_dir + pre

        sdoc2 = SDoc2Interpreter()
        sdoc2.process(file_name + '.sdoc', '')

        self.assertEqual(self.create_list_of_items(sdoc.sdoc2.node_store.get_enumerated_items()),
                         self.csv_to_tuple(file_name + '.csv'))

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug01(self):
        """
        Test case with right numeration of nodes.
        """
        self.run_test('test01.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug02(self):
        """
        Test case with wrong numeration of nodes.
        """
        self.run_test('test02.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug03(self):
        """
        Test case with different figure numeration of nodes.
        """
        self.run_test('test03.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug04(self):
        """
        Test case with item and itemize nodes.
        """
        self.run_test('test04.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug05(self):
        """
        Test case of general numbering of all type of nodes.
        """
        self.run_test('test05.sdoc')
