# Generated from sdoc/antlr/sdoc2Parser.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\24")
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\3\4\3\4\3\4\5")
        buf.write("\4\33\n\4\3\5\3\5\3\5\3\5\3\5\7\5\"\n\5\f\5\16\5%\13\5")
        buf.write("\3\5\5\5(\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\7\78\n\7\f\7\16\7;\13\7\3\7\5\7>\n\7")
        buf.write("\3\7\3\7\5\7B\n\7\3\7\5\7E\n\7\3\7\2\2\b\2\4\6\b\n\f\2")
        buf.write("\2J\2\22\3\2\2\2\4\25\3\2\2\2\6\32\3\2\2\2\b\34\3\2\2")
        buf.write("\2\n-\3\2\2\2\f\62\3\2\2\2\16\21\5\6\4\2\17\21\5\4\3\2")
        buf.write("\20\16\3\2\2\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\26\7\3")
        buf.write("\2\2\26\5\3\2\2\2\27\33\5\b\5\2\30\33\5\n\6\2\31\33\5")
        buf.write("\f\7\2\32\27\3\2\2\2\32\30\3\2\2\2\32\31\3\2\2\2\33\7")
        buf.write("\3\2\2\2\34\'\7\4\2\2\35#\7\7\2\2\36\37\7\20\2\2\37 \7")
        buf.write("\17\2\2 \"\7\21\2\2!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#")
        buf.write("$\3\2\2\2$&\3\2\2\2%#\3\2\2\2&(\7\16\2\2\'\35\3\2\2\2")
        buf.write("\'(\3\2\2\2()\3\2\2\2)*\7\b\2\2*+\7\13\2\2+,\7\n\2\2,")
        buf.write("\t\3\2\2\2-.\7\5\2\2./\7\b\2\2/\60\7\13\2\2\60\61\7\n")
        buf.write("\2\2\61\13\3\2\2\2\62=\7\6\2\2\639\7\f\2\2\64\65\7\20")
        buf.write("\2\2\65\66\7\17\2\2\668\7\21\2\2\67\64\3\2\2\28;\3\2\2")
        buf.write("\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<>\7\16\2")
        buf.write("\2=\63\3\2\2\2=>\3\2\2\2>D\3\2\2\2?A\7\r\2\2@B\7\24\2")
        buf.write("\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CE\7\23\2\2D?\3\2\2\2")
        buf.write("DE\3\2\2\2E\r\3\2\2\2\13\20\22\32#\'9=AD")
        return buf.getvalue()


class sdoc2Parser ( Parser ):

    grammarFileName = "sdoc2Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\begin'", "'\\end'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "']'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "TEXT", "BEGIN", "END", "SDOC2_COMMAND", 
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
    RULE_cmd_sdoc2 = 5

    ruleNames =  [ "sdoc", "text", "command", "cmd_begin", "cmd_end", "cmd_sdoc2" ]

    EOF = Token.EOF
    TEXT=1
    BEGIN=2
    END=3
    SDOC2_COMMAND=4
    BLOCK_ARG_LEFT_BRACKET=5
    BLOCK_ARG_LEFT_BRACE=6
    BLOCK_ARG_WS=7
    BLOCK_ARG_RIGHT_BRACE=8
    BLOCK_ARG_ARG=9
    INLINE_ARG_LEFT_BRACKET=10
    INLINE_ARG_LEFT_BRACE=11
    OPT_ARG_RIGHT_BRACKET=12
    OPT_ARG_EQUALS=13
    OPT_ARG_NAME=14
    OPT_ARG_VALUE=15
    OPT_ARG_WS=16
    INLINE_ARG_RIGHT_BRACE=17
    INLINE_ARG_ARG=18

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
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
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sdoc2Parser.TEXT) | (1 << sdoc2Parser.BEGIN) | (1 << sdoc2Parser.END) | (1 << sdoc2Parser.SDOC2_COMMAND))) != 0):
                self.state = 14
                token = self._input.LA(1)
                if token in [sdoc2Parser.BEGIN, sdoc2Parser.END, sdoc2Parser.SDOC2_COMMAND]:
                    self.state = 12
                    self.command()

                elif token in [sdoc2Parser.TEXT]:
                    self.state = 13
                    self.text()

                else:
                    raise NoViableAltException(self)

                self.state = 18
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
            self.state = 19
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
            self.state = 24
            token = self._input.LA(1)
            if token in [sdoc2Parser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.cmd_begin()

            elif token in [sdoc2Parser.END]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.cmd_end()

            elif token in [sdoc2Parser.SDOC2_COMMAND]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.cmd_sdoc2()

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
            self.state = 26
            self.match(sdoc2Parser.BEGIN)
            self.state = 37
            _la = self._input.LA(1)
            if _la==sdoc2Parser.BLOCK_ARG_LEFT_BRACKET:
                self.state = 27
                self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACKET)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sdoc2Parser.OPT_ARG_NAME:
                    self.state = 28
                    self.match(sdoc2Parser.OPT_ARG_NAME)
                    self.state = 29
                    self.match(sdoc2Parser.OPT_ARG_EQUALS)
                    self.state = 30
                    self.match(sdoc2Parser.OPT_ARG_VALUE)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(sdoc2Parser.OPT_ARG_RIGHT_BRACKET)


            self.state = 39
            self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACE)
            self.state = 40
            self.match(sdoc2Parser.BLOCK_ARG_ARG)
            self.state = 41
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
            self.state = 43
            self.match(sdoc2Parser.END)
            self.state = 44
            self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACE)
            self.state = 45
            self.match(sdoc2Parser.BLOCK_ARG_ARG)
            self.state = 46
            self.match(sdoc2Parser.BLOCK_ARG_RIGHT_BRACE)
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
        self.enterRule(localctx, 10, self.RULE_cmd_sdoc2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(sdoc2Parser.SDOC2_COMMAND)
            self.state = 59
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACKET:
                self.state = 49
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACKET)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sdoc2Parser.OPT_ARG_NAME:
                    self.state = 50
                    self.match(sdoc2Parser.OPT_ARG_NAME)
                    self.state = 51
                    self.match(sdoc2Parser.OPT_ARG_EQUALS)
                    self.state = 52
                    self.match(sdoc2Parser.OPT_ARG_VALUE)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(sdoc2Parser.OPT_ARG_RIGHT_BRACKET)


            self.state = 66
            _la = self._input.LA(1)
            if _la==sdoc2Parser.INLINE_ARG_LEFT_BRACE:
                self.state = 61
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACE)
                self.state = 63
                _la = self._input.LA(1)
                if _la==sdoc2Parser.INLINE_ARG_ARG:
                    self.state = 62
                    self.match(sdoc2Parser.INLINE_ARG_ARG)


                self.state = 65
                self.match(sdoc2Parser.INLINE_ARG_RIGHT_BRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





