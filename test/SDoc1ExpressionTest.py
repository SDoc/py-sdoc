import os

from test.SDoc1TestCase import SDoc1TestCase


class SDoc1ExpressionTest(SDoc1TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def run_test(self, sdoc_name):
        data_dir = os.path.dirname(os.path.abspath(__file__)) + '/debug/'

        with open(data_dir + sdoc_name, 'r') as file:
            sdoc1 = file.read()

        pre, ext = os.path.splitext(sdoc_name)
        text_file_name = pre + '.txt'
        with open(data_dir + text_file_name, 'r') as file:
            text = file.read()

        output = self.run_sdoc1(sdoc1)
        self.assertEqual(output, text)

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug01(self):
        """
        Test case for simple integer expression.
        """
        self.run_test('test01.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug02(self):
        """
        Test case for simple integer variable expression.
        """
        self.run_test('test02.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug03(self):
        """
        Test case for simple string expression.
        """
        self.run_test('test03.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug04(self):
        """
        Test case for undefined variable.
        """
        self.run_test('test04.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug05(self):
        """
        Test case chain expression.
        """
        self.run_test('test05.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug06(self):
        """
        Test case for simple string variable expression.
        """
        self.run_test('test06.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug07(self):
        """
        Test case for nested array expression.
        """
        self.run_test('test07.sdoc')

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug08(self):
        """
        Test case for simple array expression.
        """
        self.run_test('test08.sdoc')

# ----------------------------------------------------------------------------------------------------------------------
