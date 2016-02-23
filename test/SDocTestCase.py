import os
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

        in_stream = antlr4.InputStream(sdoc)
        out_stream = open('t.tmp', 'wt')  # @todo fix temp name

        lexer = sdoc1Lexer(in_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc1Parser(tokens)
        tree = parser.sdoc()

        visitor = SDoc1Visitor()
        visitor.set_output(out_stream)
        visitor.visit(tree)

        output = sys.stdout.getvalue().strip()

        sys.stdout = self.old_stdout

        out_stream.close()
        os.unlink('t.tmp')

        return output

# ----------------------------------------------------------------------------------------------------------------------
