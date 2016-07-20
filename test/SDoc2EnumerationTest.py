"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import ast
import csv
import glob
import os
import unittest

from cleo import Application, CommandTester

from sdoc import sdoc2
from sdoc.command.SDoc2Command import SDoc2Command
from sdoc.sdoc2 import in_scope


class SDoc2EnumerationTest(unittest.TestCase):
    """
    Test cases for SDoc2 enumerations.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_list_of_items(nodes):
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
    @staticmethod
    def csv_to_tuple(file_name):
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
    def test_numbering(self):
        """
        Runs all test cases in the test/enumeration directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/enumeration/*.sdoc")
        config_path = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/enumeration/sdoc.cfg")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                pre, ext = os.path.splitext(test_file_name)
                csv_file_name = pre + '.csv'

                application = Application()
                application.add(SDoc2Command())

                command = application.find('sdoc2')
                command_tester = CommandTester(command)
                command_tester.execute([('command', command.get_name()),
                                        ('config.cfg', config_path),
                                        ('main.sdoc2', test_file_name)])

                root = in_scope(1)
                sdoc2.node_store.number_numerable()
                numbers = root.get_enumerated_items()

                actual = self.create_list_of_items(numbers)
                expected = self.csv_to_tuple(csv_file_name)

                self.assertEqual(actual, expected)

# ----------------------------------------------------------------------------------------------------------------------
