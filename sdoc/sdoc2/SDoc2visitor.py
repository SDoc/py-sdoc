"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc import sdoc2
from sdoc.antlr.sdoc2ParserVisitor import sdoc2ParserVisitor


class SDoc2Visitor(sdoc2ParserVisitor):
    """
    Visitor for SDoc level 2.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self._output = None
        """
        Object for streaming the generated output. This object MUST implement the write method.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def set_output(self, output):
        """
        Sets the object for streaming the generated output.

        :param output: This object MUST implement the write method.
        """
        self._output = output

    # ------------------------------------------------------------------------------------------------------------------
    def stream(self, snippet):
        """
        Puts an output snippet on the output stream.

        :param str snippet: The snippet to be appended to the output stream of this parser.
        """
        if snippet is not None:
            self._output.write(snippet)

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_begin(self, ctx):
        """
        Visit a parse tree produced by a begin command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_beginContext ctx: The parse tree.
        """
        command = ctx.BLOCK_ARG_ARG().getText()

        sdoc2.node_store.create_block_node(command, {})

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_end(self, ctx):
        """
        Visit a parse tree produced by an end command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_endContext ctx: The parse tree.
        """
        command = ctx.BLOCK_ARG_ARG().getText().rstrip()

        sdoc2.node_store.end_block_node(command)

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_sdoc2(self, ctx):
        """
        Visit a parse tree produced by a inline command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_sdoc2Context ctx: The parse tree.
        """
        command = ctx.SDOC2_COMMAND().getText()
        argument = ctx.INLINE_ARG_ARG()

        sdoc2.node_store.create_inline_node(command[1:], {}, argument.getText() if argument else '')

    # ------------------------------------------------------------------------------------------------------------------
    def visitText(self, ctx):
        """
        Visit a parse tree produced by TEXT.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.TextContext ctx: The parse tree.
        """
        sdoc2.node_store.create_inline_node('TEXT', {}, ctx.TEXT().getText())


# ----------------------------------------------------------------------------------------------------------------------
