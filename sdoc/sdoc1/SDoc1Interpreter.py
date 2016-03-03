"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import os

import antlr4

from sdoc.antlr.sdoc1Lexer import sdoc1Lexer
from sdoc.antlr.sdoc1Parser import sdoc1Parser
from sdoc.sdoc1.SDoc1visitor import SDoc1Visitor


class SDoc1Interpreter:
    """
    Class for processing SDoc1 documents.
    """
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def process(infile, outfile):
        """
        Processes a SDoc1 document.

        :param str infile: The input filename with the SDoc1 document.
        :param str outfile: The output filename with the SDoc2 document.
        """
        in_stream = antlr4.FileStream(infile)
        out_stream = open(outfile, 'wt')

        lexer = sdoc1Lexer(in_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc1Parser(tokens)
        tree = parser.sdoc()
        visitor = SDoc1Visitor(root_dir=os.path.dirname(os.path.realpath(infile)))

        visitor.output = out_stream
        visitor.visit(tree)

        out_stream.close()

# ----------------------------------------------------------------------------------------------------------------------
