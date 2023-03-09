import antlr4
from cleo.io.io import IO

from sdoc import sdoc2
from sdoc.antlr.sdoc2Lexer import sdoc2Lexer
from sdoc.antlr.sdoc2Parser import sdoc2Parser
from sdoc.sdoc2.SDoc2Visitor import SDoc2Visitor


class SDoc2Interpreter:
    """
    Class for processing SDoc1 documents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO):
        """
        Object constructor.
        """

        self._io: IO = io
        """
        Styled output formatter.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def process(self, infile: str) -> int:
        """
        Processes a SDoc1 document and returns the error count.

        :param str infile: The input filename with the SDoc2 document.
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
