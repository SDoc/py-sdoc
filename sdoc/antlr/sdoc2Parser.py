# Generated from sdoc/antlr/sdoc2Parser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4\36\n\4\3\5\3\5\3\5\3\5\3\5\7\5%\n\5\f\5")
        buf.write("\16\5(\13\5\3\5\5\5+\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7;\n\7\f\7\16\7>\13\7\3\7")
        buf.write("\5\7A\n\7\3\7\3\7\5\7E\n\7\3\7\5\7H\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\bO\n\b\f\b\16\bR\13\b\3\b\5\bU\n\b\3\b\3\b\5")
        buf.write("\bY\n\b\3\b\5\b\\\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2e")
        buf.write("\2\24\3\2\2\2\4\27\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n")
        buf.write("\60\3\2\2\2\f\65\3\2\2\2\16I\3\2\2\2\20\23\5\6\4\2\21")
        buf.write("\23\5\4\3\2\22\20\3\2\2\2\22\21\3\2\2\2\23\26\3\2\2\2")
        buf.write("\24\22\3\2\2\2\24\25\3\2\2\2\25\3\3\2\2\2\26\24\3\2\2")
        buf.write("\2\27\30\7\3\2\2\30\5\3\2\2\2\31\36\5\b\5\2\32\36\5\n")
        buf.write("\6\2\33\36\5\f\7\2\34\36\5\16\b\2\35\31\3\2\2\2\35\32")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36\7\3\2\2\2\37*")
        buf.write("\7\4\2\2 &\7\b\2\2!\"\7\21\2\2\"#\7\20\2\2#%\7\22\2\2")
        buf.write("$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(")
        buf.write("&\3\2\2\2)+\7\17\2\2* \3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7")
        buf.write("\t\2\2-.\7\f\2\2./\7\13\2\2/\t\3\2\2\2\60\61\7\5\2\2\61")
        buf.write("\62\7\t\2\2\62\63\7\f\2\2\63\64\7\13\2\2\64\13\3\2\2\2")
        buf.write("\65@\7\6\2\2\66<\7\r\2\2\678\7\21\2\289\7\20\2\29;\7\22")
        buf.write("\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2")
        buf.write("\2><\3\2\2\2?A\7\17\2\2@\66\3\2\2\2@A\3\2\2\2AG\3\2\2")
        buf.write("\2BD\7\16\2\2CE\7\25\2\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2\2")
        buf.write("FH\7\24\2\2GB\3\2\2\2GH\3\2\2\2H\r\3\2\2\2IT\7\7\2\2J")
        buf.write("P\7\r\2\2KL\7\21\2\2LM\7\20\2\2MO\7\22\2\2NK\3\2\2\2O")
        buf.write("R\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2SU\7")
        buf.write("\17\2\2TJ\3\2\2\2TU\3\2\2\2U[\3\2\2\2VX\7\16\2\2WY\7\25")
        buf.write("\2\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z\\\7\24\2\2[V\3\2\2")
        buf.write("\2[\\\3\2\2\2\\\17\3\2\2\2\17\22\24\35&*<@DGPTX[")
        return buf.getvalue()


class sdoc2Parser ( Parser ):

    grammarFileName = "sdoc2Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\begin'", "'\\end'", "'\\position'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "']'", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "TEXT", "BEGIN", "END", "POSITION", "SDOC2_COMMAND", 
                      "BLOCK_ARG_LEFT_BRACKET", "BLOCK_ARG_LEFT_BRACE", 
                      "BLOCK_ARG_WS", "BLOCK_ARG_RIGHT_BRACE", "BLOCK_ARG_ARG", 
                      "INLINE_ARG_LEFT_BRACKET", "INLINE_ARG_LEFT_BRACE", 
                      "OPT_ARG_RIGHT_BRACKET", "OPT_ARG_EQUALS", "OPT_ARG_NAME", 
                      "OPT_ARG_VALUE", "OPT_ARG_WS", "INLINE_ARG_RIGHT_BRACE", 
                      "INLINE_ARG_ARG" ]

    RULE_sdoc = 0
    RULE_text = 1
    RULE_command = 2
    RULE_cmd_begin = 3
    RULE_cmd_end = 4
    RULE_cmd_position = 5
    RULE_cmd_sdoc2 = 6

    ruleNames =  [ "sdoc", "text", "command", "cmd_begin", "cmd_end", "cmd_position", 
                   "cmd_sdoc2" ]

    EOF = Token.EOF
    TEXT=1
    BEGIN=2
    END=3
    POSITION=4
    SDOC2_COMMAND=5
    BLOCK_ARG_LEFT_BRACKET=6
    BLOCK_ARG_LEFT_BRACE=7
    BLOCK_ARG_WS=8
    BLOCK_ARG_RIGHT_BRACE=9
    BLOCK_ARG_ARG=10
    INLINE_ARG_LEFT_BRACKET=11
    INLINE_ARG_LEFT_BRACE=12
    OPT_ARG_RIGHT_BRACKET=13
    OPT_ARG_EQUALS=14
    OPT_ARG_NAME=15
    OPT_ARG_VALUE=16
    OPT_ARG_WS=17
    INLINE_ARG_RIGHT_BRACE=18
    INLINE_ARG_ARG=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SdocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sdoc2Parser.CommandContext)
            else:
                return self.getTypedRuleContext(sdoc2Parser.CommandContext,i)


        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sdoc2Parser.TextContext)
            else:
                return self.getTypedRuleContext(sdoc2Parser.TextContext,i)


        def getRuleIndex(self):
            return sdoc2Parser.RULE_sdoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSdoc" ):
                return visitor.visitSdoc(self)
            else:
                return visitor.visitChildren(self)




    def sdoc(self):

        localctx = sdoc2Parser.SdocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sdoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sdoc2Parser.TEXT) | (1 << sdoc2Parser.BEGIN) | (1 << sdoc2Parser.END) | (1 << sdoc2Parser.POSITION) | (1 << sdoc2Parser.SDOC2_COMMAND))) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [sdoc2Parser.BEGIN, sdoc2Parser.END, sdoc2Parser.POSITION, sdoc2Parser.SDOC2_COMMAND]:
                    self.state = 14
                    self.command()
                    pass
                elif token in [sdoc2Parser.TEXT]:
                    self.state = 15
                    self.text()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(sdoc2Parser.TEXT, 0)

        def getRuleIndex(self):
            return sdoc2Parser.RULE_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = sdoc2Parser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(sdoc2Parser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd_begin(self):
            return self.getTypedRuleContext(sdoc2Parser.Cmd_beginContext,0)


        def cmd_end(self):
            return self.getTypedRuleContext(sdoc2Parser.Cmd_endContext,0)


        def cmd_position(self):
            return self.getTypedRuleContext(sdoc2Parser.Cmd_positionContext,0)


        def cmd_sdoc2(self):
            return self.getTypedRuleContext(sdoc2Parser.Cmd_sdoc2Context,0)


        def getRuleIndex(self):
            return sdoc2Parser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = sdoc2Parser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [sdoc2Parser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.cmd_begin()
                pass
            elif token in [sdoc2Parser.END]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.cmd_end()
                pass
            elif token in [sdoc2Parser.POSITION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.cmd_position()
                pass
            elif token in [sdoc2Parser.SDOC2_COMMAND]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.cmd_sdoc2()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_beginContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(sdoc2Parser.BEGIN, 0)

        def BLOCK_ARG_LEFT_BRACE(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_LEFT_BRACE, 0)

        def BLOCK_ARG_ARG(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_ARG, 0)

        def BLOCK_ARG_RIGHT_BRACE(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_RIGHT_BRACE, 0)

        def BLOCK_ARG_LEFT_BRACKET(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_LEFT_BRACKET, 0)

        def OPT_ARG_RIGHT_BRACKET(self):
            return self.getToken(sdoc2Parser.OPT_ARG_RIGHT_BRACKET, 0)

        def OPT_ARG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_NAME)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_NAME, i)

        def OPT_ARG_EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_EQUALS)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_EQUALS, i)

        def OPT_ARG_VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_VALUE)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_VALUE, i)

        def getRuleIndex(self):
            return sdoc2Parser.RULE_cmd_begin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_begin" ):
                return visitor.visitCmd_begin(self)
            else:
                return visitor.visitChildren(self)




    def cmd_begin(self):

        localctx = sdoc2Parser.Cmd_beginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cmd_begin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(sdoc2Parser.BEGIN)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sdoc2Parser.BLOCK_ARG_LEFT_BRACKET:
                self.state = 30
                self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACKET)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sdoc2Parser.OPT_ARG_NAME:
                    self.state = 31
                    self.match(sdoc2Parser.OPT_ARG_NAME)
                    self.state = 32
                    self.match(sdoc2Parser.OPT_ARG_EQUALS)
                    self.state = 33
                    self.match(sdoc2Parser.OPT_ARG_VALUE)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(sdoc2Parser.OPT_ARG_RIGHT_BRACKET)


            self.state = 42
            self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACE)
            self.state = 43
            self.match(sdoc2Parser.BLOCK_ARG_ARG)
            self.state = 44
            self.match(sdoc2Parser.BLOCK_ARG_RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_endContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(sdoc2Parser.END, 0)

        def BLOCK_ARG_LEFT_BRACE(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_LEFT_BRACE, 0)

        def BLOCK_ARG_ARG(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_ARG, 0)

        def BLOCK_ARG_RIGHT_BRACE(self):
            return self.getToken(sdoc2Parser.BLOCK_ARG_RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return sdoc2Parser.RULE_cmd_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_end" ):
                return visitor.visitCmd_end(self)
            else:
                return visitor.visitChildren(self)




    def cmd_end(self):

        localctx = sdoc2Parser.Cmd_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cmd_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(sdoc2Parser.END)
            self.state = 47
            self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACE)
            self.state = 48
            self.match(sdoc2Parser.BLOCK_ARG_ARG)
            self.state = 49
            self.match(sdoc2Parser.BLOCK_ARG_RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_positionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITION(self):
            return self.getToken(sdoc2Parser.POSITION, 0)

        def INLINE_ARG_LEFT_BRACKET(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_LEFT_BRACKET, 0)

        def OPT_ARG_RIGHT_BRACKET(self):
            return self.getToken(sdoc2Parser.OPT_ARG_RIGHT_BRACKET, 0)

        def INLINE_ARG_LEFT_BRACE(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_LEFT_BRACE, 0)

        def INLINE_ARG_RIGHT_BRACE(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_RIGHT_BRACE, 0)

        def OPT_ARG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_NAME)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_NAME, i)

        def OPT_ARG_EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_EQUALS)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_EQUALS, i)

        def OPT_ARG_VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_VALUE)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_VALUE, i)

        def INLINE_ARG_ARG(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_ARG, 0)

        def getRuleIndex(self):
            return sdoc2Parser.RULE_cmd_position

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_position" ):
                return visitor.visitCmd_position(self)
            else:
                return visitor.visitChildren(self)




    def cmd_position(self):

        localctx = sdoc2Parser.Cmd_positionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmd_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(sdoc2Parser.POSITION)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACKET:
                self.state = 52
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACKET)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sdoc2Parser.OPT_ARG_NAME:
                    self.state = 53
                    self.match(sdoc2Parser.OPT_ARG_NAME)
                    self.state = 54
                    self.match(sdoc2Parser.OPT_ARG_EQUALS)
                    self.state = 55
                    self.match(sdoc2Parser.OPT_ARG_VALUE)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 61
                self.match(sdoc2Parser.OPT_ARG_RIGHT_BRACKET)


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACE:
                self.state = 64
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACE)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==sdoc2Parser.INLINE_ARG_ARG:
                    self.state = 65
                    self.match(sdoc2Parser.INLINE_ARG_ARG)


                self.state = 68
                self.match(sdoc2Parser.INLINE_ARG_RIGHT_BRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_sdoc2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SDOC2_COMMAND(self):
            return self.getToken(sdoc2Parser.SDOC2_COMMAND, 0)

        def INLINE_ARG_LEFT_BRACKET(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_LEFT_BRACKET, 0)

        def OPT_ARG_RIGHT_BRACKET(self):
            return self.getToken(sdoc2Parser.OPT_ARG_RIGHT_BRACKET, 0)

        def INLINE_ARG_LEFT_BRACE(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_LEFT_BRACE, 0)

        def INLINE_ARG_RIGHT_BRACE(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_RIGHT_BRACE, 0)

        def OPT_ARG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_NAME)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_NAME, i)

        def OPT_ARG_EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_EQUALS)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_EQUALS, i)

        def OPT_ARG_VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(sdoc2Parser.OPT_ARG_VALUE)
            else:
                return self.getToken(sdoc2Parser.OPT_ARG_VALUE, i)

        def INLINE_ARG_ARG(self):
            return self.getToken(sdoc2Parser.INLINE_ARG_ARG, 0)

        def getRuleIndex(self):
            return sdoc2Parser.RULE_cmd_sdoc2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_sdoc2" ):
                return visitor.visitCmd_sdoc2(self)
            else:
                return visitor.visitChildren(self)




    def cmd_sdoc2(self):

        localctx = sdoc2Parser.Cmd_sdoc2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmd_sdoc2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(sdoc2Parser.SDOC2_COMMAND)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACKET:
                self.state = 72
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACKET)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sdoc2Parser.OPT_ARG_NAME:
                    self.state = 73
                    self.match(sdoc2Parser.OPT_ARG_NAME)
                    self.state = 74
                    self.match(sdoc2Parser.OPT_ARG_EQUALS)
                    self.state = 75
                    self.match(sdoc2Parser.OPT_ARG_VALUE)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(sdoc2Parser.OPT_ARG_RIGHT_BRACKET)


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACE:
                self.state = 84
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACE)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==sdoc2Parser.INLINE_ARG_ARG:
                    self.state = 85
                    self.match(sdoc2Parser.INLINE_ARG_ARG)


                self.state = 88
                self.match(sdoc2Parser.INLINE_ARG_RIGHT_BRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





