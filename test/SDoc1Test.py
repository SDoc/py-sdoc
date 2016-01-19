import glob
import os

from test.SDocTestCase import SDocTestCase


class SDoc1Test(SDocTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def testDebug(self):
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/debug/*.sdoc")

        for test_file_name in sorted(test_file_names):
            print(test_file_name)
            with open(test_file_name, 'r') as file:
                sdoc1 = file.read()

            pre, ext = os.path.splitext(test_file_name)
            text_file_name = pre + '.txt'
            with open(text_file_name, 'r') as file:
                text = file.read()

            output = self.run_output_test(sdoc1)
            self.assertEqual(output, text)

# ----------------------------------------------------------------------------------------------------------------------
