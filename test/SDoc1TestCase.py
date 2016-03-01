import os
import sys
import unittest
from io import StringIO
import antlr4
from sdoc.antlr.sdoc1Lexer import sdoc1Lexer
from sdoc.antlr.sdoc1Parser import sdoc1Parser
from sdoc.sdoc1.SDoc1visitor import SDoc1Visitor


class SDoc1TestCase(unittest.TestCase):
    """
    Parent class for SDoc1 test cases.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def run_sdoc1(self, sdoc):
        """
        Runs the SDoc1 parser for an SDoc document and returns the output.

        :param str sdoc: The SDoc document.

        :rtype: str
        """
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
