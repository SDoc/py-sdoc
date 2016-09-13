"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import re

from sdoc import sdoc2
from sdoc.antlr.sdoc2ParserVisitor import sdoc2ParserVisitor
from sdoc.sdoc.SDocVisitor import SDocVisitor
from sdoc.sdoc2.Position import Position


class SDoc2Visitor(sdoc2ParserVisitor, SDocVisitor):
    """
    Visitor for SDoc level 2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, sdoc1_path, io):
        """
        Object constructor.

        :param str sdoc1_path: The the path to the original SDoc1 document.
        :param cleo.styles.output_style.OutputStyle io: The IO object.
        """
        SDocVisitor.__init__(self, io)

        self._io = io
        """
        Styled output formatter.

        :type: sdoc.style.SdocStyle.SdocStyle
        """

        self._output = None
        """
        Object for streaming the generated output. This object MUST implement the write method.
        """

        self._sdoc1_file_name = sdoc1_path
        """
        The original file name at SDoc1 level.

        :type: str
        """

        self._sdoc1_line = 0
        """
        The offset of for computing the current line at SDoc1 level.

        :type: int
        """

        self._sdoc1_column = 0
        """
        The offset of for computing the current column at SDoc1 level.

        :type: int
        """

        self._sdoc2_line = 0
        """
        The line position of the last position command.

        :type: int
        """

        self._sdoc2_column = 0
        """
        The last column position of the last position command.

        :type: int
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
    def get_position(self, token):
        """
        Returns the position of the token in the original SDoc1 source file.

        :param antlr4.Token.CommonToken token:

        :rtype: sdoc.sdoc2.Position.Position
        """
        line_number = token.line
        column = token.column

        if self._sdoc2_line == line_number:
            column = self._sdoc1_column + (column - self._sdoc2_column)

        line_number = self._sdoc1_line + (line_number - self._sdoc2_line)

        return Position(self._sdoc1_file_name, line_number, column, -1, -1)

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

        sdoc2.node_store.append_block_node(command, self._get_options(ctx), self.get_position(ctx.start))

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_end(self, ctx):
        """
        Visit a parse tree produced by an end command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_endContext ctx: The parse tree.
        """
        command = ctx.BLOCK_ARG_ARG().getText().rstrip()

        sdoc2.node_store.end_block_node(command)

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_position(self, ctx):
        """
        Visit a parse tree produced by a position command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_positionContext ctx: The parse tree.
        """
        argument = ctx.INLINE_ARG_ARG()
        parts = re.match(r'(.+):([0-9]+)\.([0-9]+)', str(argument))
        if not parts:
            self._error('{0!s} is not a valid position'.format(argument))
            return

        self._sdoc1_file_name = parts.group(1)
        self._sdoc1_line = int(parts.group(2))
        self._sdoc1_column = int(parts.group(3))

        token = ctx.stop
        self._sdoc2_line = token.line
        self._sdoc2_column = token.column + len(token.text)

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_sdoc2(self, ctx):
        """
        Visit a parse tree produced by a inline command.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.Cmd_sdoc2Context ctx: The parse tree.
        """
        command = ctx.SDOC2_COMMAND().getText()
        argument = ctx.INLINE_ARG_ARG()

        sdoc2.node_store.append_inline_node(command[1:],
                                            self._get_options(ctx),
                                            argument.getText() if argument else '',
                                            self.get_position(ctx.start))

    # ------------------------------------------------------------------------------------------------------------------
    def visitText(self, ctx):
        """
        Visit a parse tree produced by TEXT.

        :param sdoc.antlr.sdoc2Parser.sdoc2Parser.TextContext ctx: The parse tree.
        """
        sdoc2.node_store.append_inline_node('TEXT', {}, ctx.TEXT().getText(), self.get_position(ctx.start))

# ----------------------------------------------------------------------------------------------------------------------
