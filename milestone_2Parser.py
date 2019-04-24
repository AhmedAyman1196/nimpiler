# Generated from milestone_2.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0083")
        buf.write("\23\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\t\2\t\fRRmmu}\177")
        buf.write("\177\u0081\u0081\u0083\u0083\16\2\n\3\2\2\2\4\f\3\2\2")
        buf.write("\2\6\16\3\2\2\2\b\20\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2")
        buf.write("\f\r\5\6\4\2\r\5\3\2\2\2\16\17\t\2\2\2\17\7\3\2\2\2\20")
        buf.write("\21\5\2\2\2\21\t\3\2\2\2\2")
        return buf.getvalue()


class milestone_2Parser ( Parser ):

    grammarFileName = "milestone_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'*'", "'-'", "'/'", 
                     "'~'", "'&'", "'|'", "'<'", "'>'", "'@'", "'%'", "'!'", 
                     "'^'", "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "<INVALID>", "'and'", "'var'", 
                     "'addr'", "'as'", "'asm'", "'bind'", "'block'", "'break'", 
                     "'case'", "'cast'", "'concept'", "'const'", "'continue'", 
                     "'converter'", "'defer'", "'discard'", "'distinct'", 
                     "'div'", "'do'", "'elif'", "'else'", "'end'", "'enum'", 
                     "'except'", "'export'", "'finally'", "'for'", "'from'", 
                     "'func'", "'if'", "'import'", "'in'", "'include'", 
                     "'interface'", "'is'", "'isnot'", "'iterator'", "'let'", 
                     "'macro'", "'method'", "'mixin'", "'mod'", "'nil'", 
                     "'not'", "'notin'", "'object'", "'of'", "'or'", "'out'", 
                     "'proc'", "'ptr'", "'raise'", "'ref'", "'return'", 
                     "'shl'", "'shr'", "'static'", "'template'", "'try'", 
                     "'tuple'", "'type'", "'using'", "'when'", "'while'", 
                     "'xor'", "'yield'" ]

    symbolicNames = [ "<INVALID>", "SKIPINDENT", "INDENT", "SPACE", "MULTILINECOMMENT", 
                      "MULTILINEDOCUMENTATION", "COMMENT", "TRIPLESTR_LIT", 
                      "STR_LIT", "CHAR_LIT", "RSTR_LIT", "GENERALIZED_STR_LIT", 
                      "GENERALIZED_TRIPLESTR_LIT", "EQUALS_OPERATOR", "ADD_OPERATOR", 
                      "MUL_OPERATOR", "MINUS_OPERATOR", "DIV_OPERATOR", 
                      "BITWISE_NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
                      "LESS_THAN", "GREATER_THAN", "AT", "MODULUS", "NOT_OPERATOR", 
                      "XOR_OPERATOR", "DOT", "COLON", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", 
                      "COMMA", "SEMI_COLON", "KEYW", "AND", "VARIABLE", 
                      "ADDR", "AS", "ASM", "BIND", "BLOCK", "BREAK", "CASE", 
                      "CAST", "CONCEPT", "CONST", "CONTINUE", "CONVERTER", 
                      "DEFER", "DISCARD", "DISTINCT", "DIV", "DO", "ELIF", 
                      "ELSE", "END", "ENUM", "EXCEPT", "EXPORT", "FINALLY", 
                      "FOR", "FROM", "FUNC", "IF", "IMPORT", "IN", "INCLUDE", 
                      "INTERFACE", "IS", "ISNOT", "ITERATOR", "LET", "MACRO", 
                      "METHOD", "MIXIN", "MOD", "NIL", "NOT", "NOTIN", "OBJECT", 
                      "OF", "OR", "OUT", "PROC", "PTR", "RAISE", "REF", 
                      "RETURN", "SHL", "SHR", "STATIC", "TEMPLATE", "TRY", 
                      "TUPLE", "TYPE", "USING", "WHEN", "WHILE", "XOR", 
                      "YIELD", "IDENTIFIER", "DIGIT", "LETTER", "INT_LIT", 
                      "HEXDIGIT", "OCTDIGIT", "BINDIGIT", "HEX_LIT", "DEC_LIT", 
                      "OCT_LIT", "BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", 
                      "INT64_LIT", "UINT_LIT", "UINT8_LIT", "UINT16_LIT", 
                      "UINT32_LIT", "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT" ]

    RULE_module = 0
    RULE_stmt = 1
    RULE_literal = 2
    RULE_start = 3

    ruleNames =  [ "module", "stmt", "literal", "start" ]

    EOF = Token.EOF
    SKIPINDENT=1
    INDENT=2
    SPACE=3
    MULTILINECOMMENT=4
    MULTILINEDOCUMENTATION=5
    COMMENT=6
    TRIPLESTR_LIT=7
    STR_LIT=8
    CHAR_LIT=9
    RSTR_LIT=10
    GENERALIZED_STR_LIT=11
    GENERALIZED_TRIPLESTR_LIT=12
    EQUALS_OPERATOR=13
    ADD_OPERATOR=14
    MUL_OPERATOR=15
    MINUS_OPERATOR=16
    DIV_OPERATOR=17
    BITWISE_NOT_OPERATOR=18
    AND_OPERATOR=19
    OR_OPERATOR=20
    LESS_THAN=21
    GREATER_THAN=22
    AT=23
    MODULUS=24
    NOT_OPERATOR=25
    XOR_OPERATOR=26
    DOT=27
    COLON=28
    OPEN_PAREN=29
    CLOSE_PAREN=30
    OPEN_BRACE=31
    CLOSE_BRACE=32
    OPEN_BRACK=33
    CLOSE_BRACK=34
    COMMA=35
    SEMI_COLON=36
    KEYW=37
    AND=38
    VARIABLE=39
    ADDR=40
    AS=41
    ASM=42
    BIND=43
    BLOCK=44
    BREAK=45
    CASE=46
    CAST=47
    CONCEPT=48
    CONST=49
    CONTINUE=50
    CONVERTER=51
    DEFER=52
    DISCARD=53
    DISTINCT=54
    DIV=55
    DO=56
    ELIF=57
    ELSE=58
    END=59
    ENUM=60
    EXCEPT=61
    EXPORT=62
    FINALLY=63
    FOR=64
    FROM=65
    FUNC=66
    IF=67
    IMPORT=68
    IN=69
    INCLUDE=70
    INTERFACE=71
    IS=72
    ISNOT=73
    ITERATOR=74
    LET=75
    MACRO=76
    METHOD=77
    MIXIN=78
    MOD=79
    NIL=80
    NOT=81
    NOTIN=82
    OBJECT=83
    OF=84
    OR=85
    OUT=86
    PROC=87
    PTR=88
    RAISE=89
    REF=90
    RETURN=91
    SHL=92
    SHR=93
    STATIC=94
    TEMPLATE=95
    TRY=96
    TUPLE=97
    TYPE=98
    USING=99
    WHEN=100
    WHILE=101
    XOR=102
    YIELD=103
    IDENTIFIER=104
    DIGIT=105
    LETTER=106
    INT_LIT=107
    HEXDIGIT=108
    OCTDIGIT=109
    BINDIGIT=110
    HEX_LIT=111
    DEC_LIT=112
    OCT_LIT=113
    BIN_LIT=114
    INT8_LIT=115
    INT16_LIT=116
    INT32_LIT=117
    INT64_LIT=118
    UINT_LIT=119
    UINT8_LIT=120
    UINT16_LIT=121
    UINT32_LIT=122
    UINT64_LIT=123
    EXP=124
    FLOAT_LIT=125
    FLOAT32_SUFFIX=126
    FLOAT32_LIT=127
    FLOAT64_SUFFIX=128
    FLOAT64_LIT=129

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ModuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(milestone_2Parser.StmtContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = milestone_2Parser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(milestone_2Parser.LiteralContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = milestone_2Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(milestone_2Parser.INT_LIT, 0)

        def INT8_LIT(self):
            return self.getToken(milestone_2Parser.INT8_LIT, 0)

        def INT16_LIT(self):
            return self.getToken(milestone_2Parser.INT16_LIT, 0)

        def INT32_LIT(self):
            return self.getToken(milestone_2Parser.INT32_LIT, 0)

        def INT64_LIT(self):
            return self.getToken(milestone_2Parser.INT64_LIT, 0)

        def UINT_LIT(self):
            return self.getToken(milestone_2Parser.UINT_LIT, 0)

        def UINT8_LIT(self):
            return self.getToken(milestone_2Parser.UINT8_LIT, 0)

        def UINT16_LIT(self):
            return self.getToken(milestone_2Parser.UINT16_LIT, 0)

        def UINT32_LIT(self):
            return self.getToken(milestone_2Parser.UINT32_LIT, 0)

        def UINT64_LIT(self):
            return self.getToken(milestone_2Parser.UINT64_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(milestone_2Parser.FLOAT_LIT, 0)

        def FLOAT32_LIT(self):
            return self.getToken(milestone_2Parser.FLOAT32_LIT, 0)

        def FLOAT64_LIT(self):
            return self.getToken(milestone_2Parser.FLOAT64_LIT, 0)

        def STR_LIT(self):
            return self.getToken(milestone_2Parser.STR_LIT, 0)

        def RSTR_LIT(self):
            return self.getToken(milestone_2Parser.RSTR_LIT, 0)

        def TRIPLESTR_LIT(self):
            return self.getToken(milestone_2Parser.TRIPLESTR_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(milestone_2Parser.CHAR_LIT, 0)

        def NIL(self):
            return self.getToken(milestone_2Parser.NIL, 0)

        def getRuleIndex(self):
            return milestone_2Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = milestone_2Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_2Parser.TRIPLESTR_LIT) | (1 << milestone_2Parser.STR_LIT) | (1 << milestone_2Parser.CHAR_LIT) | (1 << milestone_2Parser.RSTR_LIT))) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (milestone_2Parser.NIL - 80)) | (1 << (milestone_2Parser.INT_LIT - 80)) | (1 << (milestone_2Parser.INT8_LIT - 80)) | (1 << (milestone_2Parser.INT16_LIT - 80)) | (1 << (milestone_2Parser.INT32_LIT - 80)) | (1 << (milestone_2Parser.INT64_LIT - 80)) | (1 << (milestone_2Parser.UINT_LIT - 80)) | (1 << (milestone_2Parser.UINT8_LIT - 80)) | (1 << (milestone_2Parser.UINT16_LIT - 80)) | (1 << (milestone_2Parser.UINT32_LIT - 80)) | (1 << (milestone_2Parser.UINT64_LIT - 80)) | (1 << (milestone_2Parser.FLOAT_LIT - 80)) | (1 << (milestone_2Parser.FLOAT32_LIT - 80)) | (1 << (milestone_2Parser.FLOAT64_LIT - 80)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module(self):
            return self.getTypedRuleContext(milestone_2Parser.ModuleContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = milestone_2Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.module()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





