import sys
import unittest
from io import StringIO
import antlr4
from sdoc.antlr.sdoc1Lexer import sdoc1Lexer
from sdoc.antlr.sdoc1Parser import sdoc1Parser
from sdoc.sdoc1.SDoc1visitor import SDoc1Visitor


class SDocTestCase(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def run_output_test(self, sdoc):
        self.old_stdout, sys.stdout = sys.stdout, StringIO()

        stream = antlr4.InputStream(sdoc)
        lexer = sdoc1Lexer(stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc1Parser(tokens)
        tree = parser.sdoc()
        visitor = SDoc1Visitor()
        visitor.set_output(sys.stdout)
        visitor.visit(tree)

        output = sys.stdout.getvalue()

        sys.stdout = self.old_stdout

        return output

# ----------------------------------------------------------------------------------------------------------------------
