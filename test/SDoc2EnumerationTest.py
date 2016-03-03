"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import glob
import os
import ast
import csv
import unittest

from sdoc.SDoc import SDoc
from sdoc.sdoc2 import in_scope


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
    def testNumbering(self):
        """
        Runs all test cases in the test/enumeration directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/enumeration/*.sdoc")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                pre, ext = os.path.splitext(test_file_name)
                csv_file_name = pre + '.csv'

                sdoc = SDoc()
                sdoc.test_sdoc2(test_file_name)

                root = in_scope(1)
                numbers = root.get_enumerated_items()

                actual = self.create_list_of_items(numbers)
                expected = self.csv_to_tuple(csv_file_name)

                self.assertEqual(actual, expected)


# ----------------------------------------------------------------------------------------------------------------------
