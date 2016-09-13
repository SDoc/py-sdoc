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
from sdoc.antlr.sdoc1ParserVisitor import sdoc1ParserVisitor
from sdoc.helper.SDoc import SDoc
from sdoc.sdoc.SDocVisitor import SDocVisitor
from sdoc.sdoc1.data_type.ArrayDataType import ArrayDataType
from sdoc.sdoc1.data_type.IdentifierDataType import IdentifierDataType
from sdoc.sdoc1.data_type.IntegerDataType import IntegerDataType
from sdoc.sdoc1.data_type.StringDataType import StringDataType
from sdoc.sdoc1.error import DataTypeError


class SDoc1Visitor(sdoc1ParserVisitor, SDocVisitor):
    """
    Visitor for SDoc level 1.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, root_dir=os.getcwd()):
        """
        Object constructor.

        :param str root_dir: The root directory for including sub-documents.
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

        self._global_scope = ArrayDataType()
        """
        All defined variables at global scope.

        :type: sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType
        """

        self._include_level = 0
        """
        The level of including other SDoc documents.

        :type: int
        """

        self._options = {'max_include_level': 100}
        """
        The options.

        :type: dict[str,int]
        """

        self._root_dir = root_dir
        """
        The root directory for including sub-documents.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def output(self):
        """
        Getter for output.

        :rtype: T
        """
        return self._output

    # ------------------------------------------------------------------------------------------------------------------
    @output.setter
    def output(self, output):
        """
        Setter for output.

        :param T output: This object MUST implement the write method.
        """
        self._output = output

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def include_level(self):
        """
        Getter for include_level.

        :rtype: int
        """
        return self._include_level

    # ------------------------------------------------------------------------------------------------------------------
    @include_level.setter
    def include_level(self, include_level):
        """
        Setter for include_level.

        :param int include_level: The include level.
        """
        self._include_level = include_level

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def global_scope(self):
        """
        Getter for global_scope.

        :rtype: sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType
        """
        return self._global_scope

    # ------------------------------------------------------------------------------------------------------------------
    @global_scope.setter
    def global_scope(self, scope):
        """
        Setter for global_scope.

        :param sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType scope: The global scope.
        """
        self._global_scope = scope

    # ------------------------------------------------------------------------------------------------------------------
    def stream(self, snippet):
        """
        Puts an output snippet on the output stream.

        :param str snippet: The snippet to be appended to the output stream of this parser.
        """
        if snippet is not None:
            self._output.write(snippet)

    # ------------------------------------------------------------------------------------------------------------------
    def put_position(self, ctx, position):
        """
        Puts a position SDoc2 command on the output stream.

        :param antlr4.ParserRuleContext ctx: The context tree.
        :param str position: Either start or stop.
        """
        if position == 'start':
            token = ctx.start
        else:
            token = ctx.stop

        stream = token.getInputStream()
        if hasattr(stream, 'fileName'):
            # antlr4.FileStream.FileStream
            filename = stream.fileName  # Replace fileName with get_source_name() when implemented in ANTLR.
        else:
            # Input stream is a antlr4.InputStream.InputStream.
            filename = ''

        line_number = token.line
        column = token.column

        if position == 'stop':
            column += len(token.text)

        self.stream('\\position{{{0!s}:{1:d}.{2:d}}}'.format(SDoc.escape(filename), line_number, column))

    # ------------------------------------------------------------------------------------------------------------------
    def _data_is_true(self, data, token=None):
        """
        Returns True if a data type evaluates to True, False if a data type evaluates to False, and None if an error
        occurs.

        :param sdoc.sdoc1.data_type.DataType.DataType data: The data.
        :param antlr4.Token.CommonToken token: The token where data type is been used.

        :rtype: bool|None
        """
        try:
            return data.is_true()

        except DataTypeError as e:
            self._error(str(e), token)
            return None

    # ------------------------------------------------------------------------------------------------------------------
    def visit(self, tree):
        """
        Visits a parse tree produced by sdoc1

        :param antlr4.ParserRuleContext tree: The context tree.
        """
        self.put_position(tree, 'start')

        return super().visit(tree)

    # ------------------------------------------------------------------------------------------------------------------
    def visitAssignmentExpressionAssignment(self, ctx):
        """
        Visit a parse tree for expression like a = b.

        :param sdoc1Parser.AssignmentExpressionAssignmentContext ctx: The context tree.

        :rtype: mixed
        """
        right_hand_side = ctx.assignmentExpression().accept(self)
        left_hand_side = ctx.postfixExpression().accept(self)

        # Left hand side must be an identifier.
        # @todo implement array element.
        if not isinstance(left_hand_side, IdentifierDataType):
            message = "Left hand side '{0!s}' is not an identifier.".format(str(left_hand_side))
            self._error(message, ctx.postfixExpression().start)
            return

        try:
            value = left_hand_side.set_value(right_hand_side)
        except DataTypeError as e:
            self._error(str(e), ctx.assignmentExpression().start)
            return None

        return value

    # ------------------------------------------------------------------------------------------------------------------
    def visitLogicalAndExpressionAnd(self, ctx):
        """
        Visits a parse tree for expressions like 'a && b'.

        :param sdoc1Parser.LogicalAndExpressionAndContext ctx: The context tree.

        :rtype: sdoc.sdoc1.data_type.IntegerDataType.IntegerDataType
        """
        a_ctx = ctx.logicalAndExpression()
        b_ctx = ctx.equalityExpression()

        a = a_ctx.accept(self)
        b = b_ctx.accept(self)

        a_is_true = self._data_is_true(a, a_ctx.start)
        b_is_true = self._data_is_true(b, b_ctx.start)

        return IntegerDataType(1 if a_is_true and b_is_true else 0)

    # ------------------------------------------------------------------------------------------------------------------
    def visitLogicalOrExpressionLogicalOr(self, ctx):
        """
        Visits a parse tree for expressions like 'a || b'.

        :param sdoc1Parser.LogicalOrExpressionLogicalOrContext ctx: The context tree.

        :rtype: sdoc.sdoc1.data_type.IntegerDataType.IntegerDataType
        """
        a_ctx = ctx.logicalOrExpression()
        b_ctx = ctx.logicalAndExpression()

        a = a_ctx.accept(self)
        b = b_ctx.accept(self)

        a_is_true = self._data_is_true(a, a_ctx.start)
        b_is_true = self._data_is_true(b, b_ctx.start)

        return IntegerDataType(1 if a_is_true or b_is_true else 0)

    # ------------------------------------------------------------------------------------------------------------------
    def visitPostfixExpressionExpression(self, ctx):
        """
        Visits a parse tree for expressions like 'a[1]'.

        :param sdoc1Parser.PostfixExpressionExpressionContext ctx: The context tree.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        # First get the value of key.
        expression = ctx.expression().accept(self)
        if not expression.is_defined():
            message = '{0!s} is not defined.'.format(ctx.expression().getSymbol())
            self._error(message, ctx.expression().start)
            return

        postfix_expression = ctx.postfixExpression().accept(self)
        if not isinstance(postfix_expression, IdentifierDataType):
            message = "'{0!s}' is not an identifier.".format(ctx.postfixExpression().getSymbol())
            self._error(message, ctx.postfixExpression().start)
            return

        return postfix_expression.get_array_element(expression)

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionIdentifier(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#primaryExpressionIdentifier.

        :param sdoc1Parser.PrimaryExpressionIdentifierContext ctx: The context tree.

        :rtype: sdoc.sdoc1.data_type.IdentifierDataType.IdentifierDataType
        """
        return IdentifierDataType(self._global_scope, ctx.EXPR_IDENTIFIER().getText())

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionIntegerConstant(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#PrimaryExpressionIntegerConstantContext.

        :param sdoc1Parser.PrimaryExpressionIntegerConstantContext ctx: The context tree.

        :rtype: sdoc.sdoc1.data_type.IntegerDataType.IntegerDataType
        """
        return IntegerDataType(ctx.EXPR_INTEGER_CONSTANT().getText())

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionStringConstant(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#PrimaryExpressionStringConstantContext.

        :param sdoc1Parser.PrimaryExpressionStringConstantContext ctx: The context tree.

        :rtype sdoc.sdoc1.data_type.StringDataType.StringDataType
        """
        return StringDataType(ctx.EXPR_STRING_CONSTANT().getText()[1:-1].replace('\\\\', '\\').replace('\\\'', '\''))

    # ------------------------------------------------------------------------------------------------------------------
    def visitPrimaryExpressionSubExpression(self, ctx):
        """
        Visits a parse tree for sub-expressions like (a && b).

        :param sdoc1Parser.primaryExpressionSubExpression ctx: The context tree.
        """
        return ctx.expression().accept(self)

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_comment(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_comment.

        :param sdoc1Parser.Cmd_commentContext ctx: The context tree.
        """
        self.put_position(ctx, 'stop')

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_debug(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_debug.

        :param sdoc1Parser.Cmd_debugContext ctx: The context tree.
        """
        expression = ctx.expression()

        if expression is not None:
            self._io.writeln(expression.accept(self).debug())
        else:
            self._io.writeln(self._global_scope.debug())

        self.put_position(ctx, 'stop')

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_expression(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_expression.

        :param sdoc1Parser.Cmd_expressionContext ctx: The context tree.
        """
        self.visitExpression(ctx.expression())

        self.put_position(ctx, 'stop')

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_error(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_error.

        :param sdoc1Parser.Cmd_errorContext ctx: The parse tree.
        """
        token = ctx.ERROR().getSymbol()
        message = SDoc.unescape(ctx.SIMPLE_ARG().getText())

        self._error(message, token)

        self.put_position(ctx, 'stop')

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
            token_text = child.getText()
            i += 1
            if token_text in ['\\if', '\\elif']:
                # Skip {
                i += 1

                # Child is the expression to be evaluated.
                child = ctx.getChild(i)
                i += 1
                data = child.accept(self)

                # Skip }
                i += 1

                if self._data_is_true(data, child.start):
                    # Child is the code inside the if or elif clause.
                    child = ctx.getChild(i)
                    self.put_position(child, 'start')
                    i += 1
                    child.accept(self)
                    fired = True

                else:
                    # Skip the code inside the if or elif clause.
                    i += 1

            elif token_text == '\\else':
                # Child is the code inside the else clause.
                child = ctx.getChild(i)
                i += 1

                child.accept(self)
                fired = True

            elif token_text == '\\endif':
                pass

        self.put_position(ctx, 'stop')

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_include(self, ctx):
        """
        Includes another SDoc into this SDoc.

        :param sdoc1Parser.Cmd_includeContext ctx: The parse tree.
        """
        # Test the maximum include level.
        if self._include_level >= self._options['max_include_level']:
            message = 'Maximum include level exceeded'
            self._error(message, ctx.INCLUDE().getSymbol())
            return

        # Open a stream for the sub-document.
        file_name = SDoc.unescape(ctx.SIMPLE_ARG().getText())
        if not os.path.isabs(file_name):
            file_name = os.path.join(self._root_dir, file_name + '.sdoc')
        real_path = os.path.relpath(file_name)
        self._io.writeln("Including <fso>{0!s}</fso>".format(real_path))
        try:
            stream = antlr4.FileStream(file_name, 'utf-8')

            # root_dir

            # Create a new lexer and parser for the sub-document.
            lexer = sdoc1Lexer(stream)
            tokens = antlr4.CommonTokenStream(lexer)
            parser = sdoc1Parser(tokens)
            tree = parser.sdoc()

            # Create a visitor.
            visitor = SDoc1Visitor(self._io, root_dir=os.path.dirname(os.path.realpath(file_name)))

            # Set or inherit properties from the parser of the parent document.
            visitor.include_level = self._include_level + 1
            visitor.output = self._output
            visitor.global_scope = self._global_scope

            # Run the visitor on the parse tree.
            visitor.visit(tree)

            # Copy  properties from the child document.
            self._errors += visitor.errors

            self.put_position(ctx, 'stop')
        except FileNotFoundError as e:
            message = 'Unable to open file {0!s}.\nCause: {1!s}'.format(real_path, e)
            self._error(message, ctx.INCLUDE().getSymbol())

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_notice(self, ctx):
        """
        Visits a parse tree produced by sdoc1Parser#cmd_notice.

        :param sdoc1Parser.Cmd_noticeContext ctx: The parse tree.
        """
        token = ctx.NOTICE().getSymbol()
        filename = token.getInputStream().fileName  # Replace fileName with get_source_name() when implemented in ANTLR.
        line_number = token.line
        message = SDoc.unescape(ctx.SIMPLE_ARG().getText())

        self._io.writeln(
            '<notice>Notice: {0!s} at {1!s}:{2:d}</notice>'.format(message, os.path.relpath(filename), line_number))

        self.put_position(ctx, 'stop')

    # ------------------------------------------------------------------------------------------------------------------
    def visitCmd_substitute(self, ctx):
        """
        Visit a parse tree produced by sdoc1Parser#cmd_substitute.

        :param sdoc1Parser.Cmd_substituteContext ctx:  The parse tree.
        """
        expression = ctx.expression()
        self.stream(expression.accept(self).get_value())

        self.put_position(ctx, 'stop')

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
