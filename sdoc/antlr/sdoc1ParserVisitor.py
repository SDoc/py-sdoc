# Generated from sdoc/antlr/sdoc1Parser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sdoc1Parser import sdoc1Parser
else:
    from sdoc1Parser import sdoc1Parser

# This class defines a complete generic visitor for a parse tree produced by sdoc1Parser.

class sdoc1ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sdoc1Parser#sdoc.
    def visitSdoc(self, ctx:sdoc1Parser.SdocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#text.
    def visitText(self, ctx:sdoc1Parser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#command.
    def visitCommand(self, ctx:sdoc1Parser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_comment.
    def visitCmd_comment(self, ctx:sdoc1Parser.Cmd_commentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_debug.
    def visitCmd_debug(self, ctx:sdoc1Parser.Cmd_debugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_expression.
    def visitCmd_expression(self, ctx:sdoc1Parser.Cmd_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_error.
    def visitCmd_error(self, ctx:sdoc1Parser.Cmd_errorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_if.
    def visitCmd_if(self, ctx:sdoc1Parser.Cmd_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_include.
    def visitCmd_include(self, ctx:sdoc1Parser.Cmd_includeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_notice.
    def visitCmd_notice(self, ctx:sdoc1Parser.Cmd_noticeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_substitute.
    def visitCmd_substitute(self, ctx:sdoc1Parser.Cmd_substituteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#cmd_sdoc2.
    def visitCmd_sdoc2(self, ctx:sdoc1Parser.Cmd_sdoc2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#primaryExpressionIdentifier.
    def visitPrimaryExpressionIdentifier(self, ctx:sdoc1Parser.PrimaryExpressionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#primaryExpressionIntegerConstant.
    def visitPrimaryExpressionIntegerConstant(self, ctx:sdoc1Parser.PrimaryExpressionIntegerConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#primaryExpressionStringConstant.
    def visitPrimaryExpressionStringConstant(self, ctx:sdoc1Parser.PrimaryExpressionStringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#primaryExpressionSubExpression.
    def visitPrimaryExpressionSubExpression(self, ctx:sdoc1Parser.PrimaryExpressionSubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#primaryExpressionParent.
    def visitPrimaryExpressionParent(self, ctx:sdoc1Parser.PrimaryExpressionParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#postfixExpressionExpression.
    def visitPostfixExpressionExpression(self, ctx:sdoc1Parser.PostfixExpressionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:sdoc1Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:sdoc1Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:sdoc1Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#equalityExpression.
    def visitEqualityExpression(self, ctx:sdoc1Parser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#logicalAndExpressionParent.
    def visitLogicalAndExpressionParent(self, ctx:sdoc1Parser.LogicalAndExpressionParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#logicalAndExpressionAnd.
    def visitLogicalAndExpressionAnd(self, ctx:sdoc1Parser.LogicalAndExpressionAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#logicalOrExpressionParent.
    def visitLogicalOrExpressionParent(self, ctx:sdoc1Parser.LogicalOrExpressionParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#logicalOrExpressionLogicalOr.
    def visitLogicalOrExpressionLogicalOr(self, ctx:sdoc1Parser.LogicalOrExpressionLogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#assignmentExpressionParent.
    def visitAssignmentExpressionParent(self, ctx:sdoc1Parser.AssignmentExpressionParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#assignmentExpressionAssignment.
    def visitAssignmentExpressionAssignment(self, ctx:sdoc1Parser.AssignmentExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:sdoc1Parser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc1Parser#expression.
    def visitExpression(self, ctx:sdoc1Parser.ExpressionContext):
        return self.visitChildren(ctx)



del sdoc1Parser