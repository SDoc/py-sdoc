"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import antlr4

from sdoc import sdoc2
from sdoc.antlr.sdoc2Lexer import sdoc2Lexer
from sdoc.antlr.sdoc2Parser import sdoc2Parser
from sdoc.sdoc2.SDoc2Visitor import SDoc2Visitor


class SDoc2Interpreter:
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
    def process(self, infile):
        """
        Processes a SDoc1 document.

        :param str infile: The input filename with the SDoc2 document.

        :rtype: int The count of errors.
        """
        in_stream = antlr4.FileStream(infile, 'utf-8')

        lexer = sdoc2Lexer(in_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc2Parser(tokens)
        tree = parser.sdoc()
        visitor = SDoc2Visitor(infile, self._io)

        visitor.visit(tree)

        sdoc2.node_store.prepare_content_tree()

        return visitor.errors

# ----------------------------------------------------------------------------------------------------------------------
