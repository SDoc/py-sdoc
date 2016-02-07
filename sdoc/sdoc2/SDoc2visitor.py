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
    @staticmethod
    def _get_options(ctx):
        """
        Returns the option of an command.

        :param ParserRuleContext ctx: The parse tree with the options.

        :rtype: dict[str,str]
        """
        options = {}
        i = 0
        while True:
            name_token = ctx.OPT_ARG_NAME(i)
            value_token = ctx.OPT_ARG_VALUE(i)
            if not name_token:
                break

            option_name = name_token.getText()
            option_value = value_token.getText()
            # Trim leading and trailing (double)quotes from string. (Is there a way to do this in ANTLR?)
            if (option_value[0] == '"' and option_value[-1] == '"') or \
                    (option_value[0] == "'" and option_value[-1] == "'"):
                option_value = option_value[1:-1]

            options[option_name] = option_value
            i += 1

        return options

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

        sdoc2.node_store.append_block_node(command, self._get_options(ctx))

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

        sdoc2.node_store.append_inline_node(command[1:], self._get_options(ctx), argument.getText() if argument else '')

    # ------------------------------------------------------------------------------------------------------------------
    def visitText(self, ctx):
        """
        Visit a parse tree produced by TEXT.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.TextContext ctx: The parse tree.
        """
        sdoc2.node_store.append_inline_node('TEXT', {}, ctx.TEXT().getText())

# ----------------------------------------------------------------------------------------------------------------------
