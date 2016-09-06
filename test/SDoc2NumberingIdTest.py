"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import glob
import os
import unittest

from cleo import Application, CommandTester

from sdoc.command.SDocCommand import SDocCommand


class SDoc2NumberingIdTest(unittest.TestCase):
    """
    Test cases for SDoc2 numbering of ID's.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_numbering_id(self):
        """
        Runs all test cases in the test/numbering_id directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/numbering_id/*.sdoc")
        config_path = os.path.dirname(os.path.abspath(__file__)) + "/numbering_id/sdoc.cfg"

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                application = Application()
                application.add(SDocCommand())

                command = application.find('sdoc')
                command_tester = CommandTester(command)
                status = command_tester.execute([('command', command.get_name()),
                                                 ('config.cfg', config_path),
                                                 ('main.sdoc', test_file_name)])

                with open('output.html', 'r') as actual:
                    actual_text = actual.read()

                print(actual_text)

                self.assertIn('<h1 id="#chapter:1">1 chapter 1</h1>', actual_text)
                self.assertIn('<h2 id="#section:1.1">1.1 ololol</h2>', actual_text)
                self.assertIn('<div class="part" id="#part:1-1">1 First part</div>', actual_text)
                self.assertIn('<h1 id="#chapter:1-1">1 Cchapter 2</h1>', actual_text)
                self.assertIn('<h2 id="#section:1-1.1">1.1 ololol2</h2>', actual_text)
                self.assertIn('<div class="part" id="#part:2-2">2 Second part, YEAH!!!</div>', actual_text)
                self.assertIn('<h1 id="#chapter:2-1">1 CHAPTER 1</h1>', actual_text)
                self.assertIn('<h2 id="#section:2-1.1">1.1 section12</h2>', actual_text)

# ----------------------------------------------------------------------------------------------------------------------
