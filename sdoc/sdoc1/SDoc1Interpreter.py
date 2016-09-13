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
from sdoc.sdoc1.SDoc1Visitor import SDoc1Visitor


class SDoc1Interpreter:
    """
    Class for processing SDoc1 documents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io):
        """
        Object constructor.
        """

        self._io = io
        """
        Styled output formatter.

        :type: sdoc.style.SdocStyle.SdocStyle
        """

    # ------------------------------------------------------------------------------------------------------------------
    def process(self, infile, outfile):
        """
        Processes a SDoc1 document.

        :param str infile: The input filename with the SDoc1 document.
        :param str outfile: The output filename with the SDoc2 document.

        :rtype: int
        """
        in_stream = antlr4.FileStream(infile)

        self._io.writeln('Writing <fso>{0!s}</fso>'.format(outfile))
        with open(outfile, 'wt') as out_stream:
            lexer = sdoc1Lexer(in_stream)
            tokens = antlr4.CommonTokenStream(lexer)
            parser = sdoc1Parser(tokens)
            tree = parser.sdoc()

            visitor = SDoc1Visitor(self._io, root_dir=os.path.dirname(os.path.realpath(infile)))

            visitor.output = out_stream
            visitor.visit(tree)

            return visitor.errors

# ----------------------------------------------------------------------------------------------------------------------
