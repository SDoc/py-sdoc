# Generated from sdoc/antlr/sdoc2Parser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,1,1,1,1,2,1,2,1,2,1,2,3,
        2,28,8,2,1,3,1,3,1,3,1,3,1,3,5,3,35,8,3,10,3,12,3,38,9,3,1,3,3,3,
        41,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,
        5,57,8,5,10,5,12,5,60,9,5,1,5,3,5,63,8,5,1,5,1,5,3,5,67,8,5,1,5,
        3,5,70,8,5,1,6,1,6,1,6,1,6,1,6,5,6,77,8,6,10,6,12,6,80,9,6,1,6,3,
        6,83,8,6,1,6,1,6,3,6,87,8,6,1,6,3,6,90,8,6,1,6,0,0,7,0,2,4,6,8,10,
        12,0,0,99,0,18,1,0,0,0,2,21,1,0,0,0,4,27,1,0,0,0,6,29,1,0,0,0,8,
        46,1,0,0,0,10,51,1,0,0,0,12,71,1,0,0,0,14,17,3,4,2,0,15,17,3,2,1,
        0,16,14,1,0,0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,
        1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,21,22,5,1,0,0,22,3,1,0,0,0,23,
        28,3,6,3,0,24,28,3,8,4,0,25,28,3,10,5,0,26,28,3,12,6,0,27,23,1,0,
        0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,5,1,0,0,0,29,40,
        5,2,0,0,30,36,5,6,0,0,31,32,5,15,0,0,32,33,5,14,0,0,33,35,5,16,0,
        0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,
        1,0,0,0,38,36,1,0,0,0,39,41,5,13,0,0,40,30,1,0,0,0,40,41,1,0,0,0,
        41,42,1,0,0,0,42,43,5,7,0,0,43,44,5,10,0,0,44,45,5,9,0,0,45,7,1,
        0,0,0,46,47,5,3,0,0,47,48,5,7,0,0,48,49,5,10,0,0,49,50,5,9,0,0,50,
        9,1,0,0,0,51,62,5,4,0,0,52,58,5,11,0,0,53,54,5,15,0,0,54,55,5,14,
        0,0,55,57,5,16,0,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,
        59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,63,5,13,0,0,62,52,1,0,
        0,0,62,63,1,0,0,0,63,69,1,0,0,0,64,66,5,12,0,0,65,67,5,19,0,0,66,
        65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,70,5,18,0,0,69,64,1,0,
        0,0,69,70,1,0,0,0,70,11,1,0,0,0,71,82,5,5,0,0,72,78,5,11,0,0,73,
        74,5,15,0,0,74,75,5,14,0,0,75,77,5,16,0,0,76,73,1,0,0,0,77,80,1,
        0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,
        83,5,13,0,0,82,72,1,0,0,0,82,83,1,0,0,0,83,89,1,0,0,0,84,86,5,12,
        0,0,85,87,5,19,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,
        90,5,18,0,0,89,84,1,0,0,0,89,90,1,0,0,0,90,13,1,0,0,0,13,16,18,27,
        36,40,58,62,66,69,78,82,86,89
    ]

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
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SdocContext(ParserRuleContext):
        __slots__ = 'parser'

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4, 5]:
                    self.state = 14
                    self.command()
                    pass
                elif token in [1]:
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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.cmd_begin()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.cmd_end()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.cmd_position()
                pass
            elif token in [5]:
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
        __slots__ = 'parser'

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
            if _la==6:
                self.state = 30
                self.match(sdoc2Parser.BLOCK_ARG_LEFT_BRACKET)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
            if _la==11:
                self.state = 52
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACKET)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
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
            if _la==12:
                self.state = 64
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACE)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
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
        __slots__ = 'parser'

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
            if _la==11:
                self.state = 72
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACKET)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
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
            if _la==12:
                self.state = 84
                self.match(sdoc2Parser.INLINE_ARG_LEFT_BRACE)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
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





