# Generated from sdoc/antlr/sdoc2Parser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sdoc2Parser import sdoc2Parser
else:
    from sdoc2Parser import sdoc2Parser

# This class defines a complete generic visitor for a parse tree produced by sdoc2Parser.

class sdoc2ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sdoc2Parser#sdoc.
    def visitSdoc(self, ctx:sdoc2Parser.SdocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#text.
    def visitText(self, ctx:sdoc2Parser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#command.
    def visitCommand(self, ctx:sdoc2Parser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#cmd_begin.
    def visitCmd_begin(self, ctx:sdoc2Parser.Cmd_beginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#cmd_end.
    def visitCmd_end(self, ctx:sdoc2Parser.Cmd_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#cmd_position.
    def visitCmd_position(self, ctx:sdoc2Parser.Cmd_positionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sdoc2Parser#cmd_sdoc2.
    def visitCmd_sdoc2(self, ctx:sdoc2Parser.Cmd_sdoc2Context):
        return self.visitChildren(ctx)



del sdoc2Parser