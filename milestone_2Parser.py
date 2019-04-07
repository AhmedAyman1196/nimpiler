# Generated from milestone_2.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0082")
        buf.write("\17\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\2\2\5\2\4\6\2\2\2\13\2\b\3\2\2\2\4\n\3\2\2\2\6\f\3")
        buf.write("\2\2\2\b\t\5\4\3\2\t\3\3\2\2\2\n\13\7(\2\2\13\5\3\2\2")
        buf.write("\2\f\r\5\2\2\2\r\7\3\2\2\2\2")
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
                     "']'", "','", "';'", "'and'", "'var'", "'addr'", "'as'", 
                     "'asm'", "'bind'", "'block'", "'break'", "'case'", 
                     "'cast'", "'concept'", "'const'", "'continue'", "'converter'", 
                     "'defer'", "'discard'", "'distinct'", "'div'", "'do'", 
                     "'elif'", "'else'", "'end'", "'enum'", "'except'", 
                     "'export'", "'finally'", "'for'", "'from'", "'func'", 
                     "'if'", "'import'", "'in'", "'include'", "'interface'", 
                     "'is'", "'isnot'", "'iterator'", "'let'", "'macro'", 
                     "'method'", "'mixin'", "'mod'", "'nil'", "'not'", "'notin'", 
                     "'object'", "'of'", "'or'", "'out'", "'proc'", "'ptr'", 
                     "'raise'", "'ref'", "'return'", "'shl'", "'shr'", "'static'", 
                     "'template'", "'try'", "'tuple'", "'type'", "'using'", 
                     "'when'", "'while'", "'xor'", "'yield'" ]

    symbolicNames = [ "<INVALID>", "SKIPINDENT", "INDENT", "SPACE", "MULTILINECOMMENT", 
                      "MULTILINEDOCUMENTATION", "COMMENT", "TRIPLESTR_LIT", 
                      "STR_LIT", "CHAR_LIT", "RSTR_LIT", "GENERALIZED_STR_LIT", 
                      "GENERALIZED_TRIPLESTR_LIT", "EQUALS_OPERATOR", "ADD_OPERATOR", 
                      "MUL_OPERATOR", "MINUS_OPERATOR", "DIV_OPERATOR", 
                      "BITWISE_NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
                      "LESS_THAN", "GREATER_THAN", "AT", "MODULUS", "NOT_OPERATOR", 
                      "XOR_OPERATOR", "DOT", "COLON", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", 
                      "COMMA", "SEMI_COLON", "AND", "VARIABLE", "ADDR", 
                      "AS", "ASM", "BIND", "BLOCK", "BREAK", "CASE", "CAST", 
                      "CONCEPT", "CONST", "CONTINUE", "CONVERTER", "DEFER", 
                      "DISCARD", "DISTINCT", "DIV", "DO", "ELIF", "ELSE", 
                      "END", "ENUM", "EXCEPT", "EXPORT", "FINALLY", "FOR", 
                      "FROM", "FUNC", "IF", "IMPORT", "IN", "INCLUDE", "INTERFACE", 
                      "IS", "ISNOT", "ITERATOR", "LET", "MACRO", "METHOD", 
                      "MIXIN", "MOD", "NIL", "NOT", "NOTIN", "OBJECT", "OF", 
                      "OR", "OUT", "PROC", "PTR", "RAISE", "REF", "RETURN", 
                      "SHL", "SHR", "STATIC", "TEMPLATE", "TRY", "TUPLE", 
                      "TYPE", "USING", "WHEN", "WHILE", "XOR", "YIELD", 
                      "IDENTIFIER", "DIGIT", "LETTER", "INT_LIT", "HEXDIGIT", 
                      "OCTDIGIT", "BINDIGIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", 
                      "BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT" ]

    RULE_stmt = 0
    RULE_complexOrSimpleStmt = 1
    RULE_start = 2

    ruleNames =  [ "stmt", "complexOrSimpleStmt", "start" ]

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
    AND=37
    VARIABLE=38
    ADDR=39
    AS=40
    ASM=41
    BIND=42
    BLOCK=43
    BREAK=44
    CASE=45
    CAST=46
    CONCEPT=47
    CONST=48
    CONTINUE=49
    CONVERTER=50
    DEFER=51
    DISCARD=52
    DISTINCT=53
    DIV=54
    DO=55
    ELIF=56
    ELSE=57
    END=58
    ENUM=59
    EXCEPT=60
    EXPORT=61
    FINALLY=62
    FOR=63
    FROM=64
    FUNC=65
    IF=66
    IMPORT=67
    IN=68
    INCLUDE=69
    INTERFACE=70
    IS=71
    ISNOT=72
    ITERATOR=73
    LET=74
    MACRO=75
    METHOD=76
    MIXIN=77
    MOD=78
    NIL=79
    NOT=80
    NOTIN=81
    OBJECT=82
    OF=83
    OR=84
    OUT=85
    PROC=86
    PTR=87
    RAISE=88
    REF=89
    RETURN=90
    SHL=91
    SHR=92
    STATIC=93
    TEMPLATE=94
    TRY=95
    TUPLE=96
    TYPE=97
    USING=98
    WHEN=99
    WHILE=100
    XOR=101
    YIELD=102
    IDENTIFIER=103
    DIGIT=104
    LETTER=105
    INT_LIT=106
    HEXDIGIT=107
    OCTDIGIT=108
    BINDIGIT=109
    HEX_LIT=110
    DEC_LIT=111
    OCT_LIT=112
    BIN_LIT=113
    INT8_LIT=114
    INT16_LIT=115
    INT32_LIT=116
    INT64_LIT=117
    UINT_LIT=118
    UINT8_LIT=119
    UINT16_LIT=120
    UINT32_LIT=121
    UINT64_LIT=122
    EXP=123
    FLOAT_LIT=124
    FLOAT32_SUFFIX=125
    FLOAT32_LIT=126
    FLOAT64_SUFFIX=127
    FLOAT64_LIT=128

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complexOrSimpleStmt(self):
            return self.getTypedRuleContext(milestone_2Parser.ComplexOrSimpleStmtContext,0)


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
        self.enterRule(localctx, 0, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.complexOrSimpleStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexOrSimpleStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(milestone_2Parser.VARIABLE, 0)

        def getRuleIndex(self):
            return milestone_2Parser.RULE_complexOrSimpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexOrSimpleStmt" ):
                listener.enterComplexOrSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexOrSimpleStmt" ):
                listener.exitComplexOrSimpleStmt(self)




    def complexOrSimpleStmt(self):

        localctx = milestone_2Parser.ComplexOrSimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_complexOrSimpleStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(milestone_2Parser.VARIABLE)
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

        def stmt(self):
            return self.getTypedRuleContext(milestone_2Parser.StmtContext,0)


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
        self.enterRule(localctx, 4, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





