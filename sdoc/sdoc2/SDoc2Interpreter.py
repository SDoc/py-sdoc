"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import os

import antlr4

import sdoc
from sdoc.antlr.sdoc2Lexer import sdoc2Lexer
from sdoc.antlr.sdoc2Parser import sdoc2Parser
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.SDoc2visitor import SDoc2Visitor


class SDoc2Interpreter:
    """
    Class for processing SDoc1 documents.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        # Create node store.
        sdoc.sdoc2.node_store = NodeStore()

        # Import all node modules.
        self.importing('/node/')
        self.importing('/formatter/html/')

    # ------------------------------------------------------------------------------------------------------------------
    def importing(self, path):
        """
        Imports modules from specific path.

        :param str path: The specific path.
        """
        modules = os.listdir(os.path.dirname(__file__) + path)

        path = path.replace('/', '.')

        for module in modules:
            if module != '__init__.py' and module[-3:] == '.py':
                __import__('sdoc.sdoc2' + path + module[:-3], locals(), globals())

    # ------------------------------------------------------------------------------------------------------------------
    def process(self, infile, outfile):
        """
        Processes a SDoc1 document.

        :param str infile: The input filename with the SDoc2 document.
        :param str outfile: The output filename with the target document.
        """
        in_stream = antlr4.FileStream(infile, 'utf-8')

        lexer = sdoc2Lexer(in_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc2Parser(tokens)
        tree = parser.sdoc()
        visitor = SDoc2Visitor()

        visitor.visit(tree)

        sdoc.sdoc2.node_store.prepare_content_tree()


# ----------------------------------------------------------------------------------------------------------------------
