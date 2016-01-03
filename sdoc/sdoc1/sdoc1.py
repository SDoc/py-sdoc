from sdoc.antlr.sdoc1Parser import sdoc1Parser
from sdoc.antlr.sdoc1ParserVisitor import sdoc1ParserVisitor
from sdoc.sdoc1.data_type.ArrayDataType import ArrayDataType
from sdoc.sdoc1.data_type.IdentifierDataType import IdentifierDataType
from sdoc.sdoc1.data_type.IntegerDataType import IntegerDataType
from sdoc.sdoc1.data_type.StringDataType import StringDataType


class Sdoc1(sdoc1ParserVisitor):
    """
    Visitor for SDoc level 1.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self._output = ''
        """
        The generated output.

        :type: str
        """

        self._variables = ArrayDataType()
        """
        All defined variables and constants.

        :type: sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType
        """

    # ------------------------------------------------------------------------------------------------------------------
    def stream(self, snippet):
        """
        Puts a output snippet on the output stream.

        :param str snippet: The snippet to be appended to the output stream of this parser.
        """
        if snippet is not None:
            self._output += snippet

    # ------------------------------------------------------------------------------------------------------------------
    def visitAssignmentExpressionAssignment(self, ctx):
        """
        Visit a parse tree produced by sdoc1Parser#assignmentExpressionAssignment.

        :param sdoc1Parser.AssignmentExpressionAssignmentContext ctx: The context tree.
        """
        right_hand_side = ctx.assignmentExpression().accept(self)
        left_hand_side = ctx.postfixExpression().accept(self)

        # Left hand side must be an identifier.
        # @todo implement array element.
        if not isinstance(left_hand_side, IdentifierDataType):
            raise RuntimeError("Left hand side '%s' is not an identifier." % str(left_hand_side))

        return left_hand_side.set_value(right_hand_side)

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionIdentifier(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#primaryExpressionIdentifier.

        :param sdoc1Parser.PrimaryExpressionIdentifierContext ctx: The context tree.
        """
        return IdentifierDataType(self._variables, ctx.IDENTIFIER().getText())

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionIntegerConstant(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#PrimaryExpressionIntegerConstantContext.

        :param sdoc1Parser.PrimaryExpressionIntegerConstantContext ctx: The context tree.
        """
        return IntegerDataType(ctx.INTEGER_CONSTANT().getText())

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionStringConstant(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#PrimaryExpressionStringConstantContext.

        :param sdoc1Parser.PrimaryExpressionStringConstantContext ctx: The context tree.
        """
        return StringDataType(ctx.STRING_CONSTANT().getText()[1:-1])

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_comment(self, ctx: sdoc1Parser.Cmd_commentContext):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_comment.

        :param sdoc1Parser.Cmd_commentContext ctx: The context tree.
        """
        # @todo If previous char is not a new line (i.e. middle in the line comment) print newline
        # @todo otherwise print new line

        self.stream('')
        # @todo set position

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_debug(self, ctx:sdoc1Parser.Cmd_debugContext):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_debug.

        :param sdoc1Parser.Cmd_debugContext ctx: The context tree.
        """
        expression = ctx.expression()

        if expression is not None:
            print(expression.accept(self).debug())
        else:
            print(self._variables.debug())

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_expression(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_expression.

        :param sdoc1Parser.Cmd_expressionContext ctx: The context tree.
        """
        self.visitExpression(ctx.expression())
        # @todo set position

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_if(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_if.

        :param sdoc1Parser.Cmd_ifContext ctx: The parse tree.
        """
        n = ctx.getChildCount()
        fired = False
        i = 0
        while i < n and not fired:
            child = ctx.getChild(i)
            token = child.getText()
            i += 1
            if token == '\\if' or token == '\\elif':
                # Skip {
                i += 1

                # Child is the expression to be evaluated.
                child = ctx.getChild(i)
                i += 1
                data = child.accept(self)
                """
                :type: sdoc.sdoc1.data_type.DataType.DataType
                """

                # Skip }
                i += 1

                if data.is_true():
                    # Child is the code inside the if or elif clause.
                    child = ctx.getChild(i)
                    i += 1
                    child.accept(self)
                    fired = True

                else:
                    # Skip the code inside the if or elif clause.
                    i += 1

            elif token == '\\else':
                # Child is the code inside the else clause.
                child = ctx.getChild(i)
                i += 1

                child.accept(self)
                fired = True

            elif token == '\\endif':
                # @todo set position
                pass

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_notice(self, ctx: sdoc1Parser.Cmd_noticeContext):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_notice.

        :param sdoc1Parser.Cmd_noticeContext ctx: The parse tree.
        """
        # @todo print position
        print('Notice: ' + ctx.NOTICE_MESSAGE().getText())
        # @todo set position

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_sdoc2(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#sdoc2_cmd.

        :param sdoc1Parser.Cmd_sdoc2Context ctx: The parse tree.
        """
        self.stream(ctx.SDOC2_COMMAND().getText())

    # ------------------------------------------------------------------------------------------------------------------
    def visitText(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#text.

        :param sdoc1Parser.TextContext ctx: The parse tree.
        """
        self.stream(ctx.TEXT().getText())

# ----------------------------------------------------------------------------------------------------------------------
