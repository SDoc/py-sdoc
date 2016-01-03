from test.SDocTestCase import SDocTestCase


class SDoc1Test(SDocTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        sdoc1 = """
\expression{a=1}
\debug{a}
"""
        output = self.run_output_test(sdoc1)
        self.assertEqual(output, "'a' => 1")

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        sdoc1 = """
\expression{a=b=c='abc'}
\debug{a}
\debug{b}
\debug{c}
"""
        expected = """'a' => 'abc'
'b' => 'abc'
'c' => 'abc'"""

        output = self.run_output_test(sdoc1)
        self.assertEqual(output, expected)


# ----------------------------------------------------------------------------------------------------------------------
