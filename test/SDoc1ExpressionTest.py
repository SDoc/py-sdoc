"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import glob
import os
import unittest

from sdoc.SDoc import SDoc


class SDoc1ExpressionTest(unittest.TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug(self):
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

                sdoc = SDoc()
                (stdout, sdoc2) = sdoc.test_sdoc1(test_file_name)

                self.assertEqual(stdout, text)


# ----------------------------------------------------------------------------------------------------------------------
