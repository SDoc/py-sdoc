import glob
import os
import unittest

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDoc1Command import SDoc1Command


class SDoc1ExpressionTest(unittest.TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_debug(self):
        """
        Runs all test cases in the test/debug directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/debug/*.sdoc")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                pre, ext = os.path.splitext(test_file_name)
                text_file_name = pre + '.txt'
                with open(text_file_name, 'r') as file:
                    text = file.read()

                application = Application()
                application.add(SDoc1Command())

                command = application.find('sdoc1')
                command_tester = CommandTester(command)
                command_tester.execute('{} t.sdoc2'.format(test_file_name))

                self.assertTrue(command_tester.io.fetch_output().rstrip().endswith(text.strip()))

# ----------------------------------------------------------------------------------------------------------------------
