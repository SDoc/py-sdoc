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


class SDoc2ReferencesTest(unittest.TestCase):
    """
    Test cases for SDoc2 references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_references(self):
        """
        Runs all test cases in test/refs directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/refs/*.sdoc')
        config_path = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/refs/sdoc.cfg')

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                application = Application()
                application.add(SDocCommand())

                command = application.find('sdoc')
                command_tester = CommandTester(command)
                command_tester.execute([('command', command.get_name()),
                                        ('config.cfg', config_path),
                                        ('main.sdoc', test_file_name)])

                with open('output.html', 'r') as actual:
                    actual_text = actual.read()

                self.assertIn('<h3 id="chap:intro">1 Introduction</h3>', actual_text)
                self.assertIn('chapter <a class="sdoc.reference" href="#chap:awesome" title="Awesome">2</a>', actual_text)
                self.assertIn('<h3 id="chap:awesome">2 Awesome</h3>', actual_text)
                self.assertIn('chapter <a class="sdoc.reference" href="#chap:intro" title="Introduction">1</a>', actual_text)

# ----------------------------------------------------------------------------------------------------------------------
