# Generated from milestone_2.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0086")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\5\b8\n\b\3\b\3\b\3\b\5\b=\n\b\7\b?\n\b")
        buf.write("\f\b\16\bB\13\b\3\t\3\t\3\t\3\t\5\tH\n\t\3\t\3\t\3\t\5")
        buf.write("\tM\n\t\7\tO\n\t\f\t\16\tR\13\t\3\t\3\t\3\n\3\n\3\n\2")
        buf.write("\2\13\2\4\6\b\n\f\16\20\22\2\3\t\2\f\17UUppx\u0080\u0082")
        buf.write("\u0082\u0084\u0084\u0086\u0086Y\2\25\3\2\2\2\4\34\3\2")
        buf.write("\2\2\6\36\3\2\2\2\b-\3\2\2\2\n\61\3\2\2\2\f\63\3\2\2\2")
        buf.write("\16\67\3\2\2\2\20C\3\2\2\2\22U\3\2\2\2\24\26\5\4\3\2\25")
        buf.write("\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\3\3\2\2\2\31\35\5\6\4\2\32\35\5\b\5\2\33\35\5\20\t")
        buf.write("\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35\5\3\2")
        buf.write("\2\2\36\37\7\3\2\2\37$\7m\2\2 !\7(\2\2!#\7m\2\2\" \3\2")
        buf.write("\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%+\3\2\2\2&$\3\2\2")
        buf.write("\2\'(\7!\2\2(,\7\4\2\2)*\7\5\2\2*,\5\n\6\2+\'\3\2\2\2")
        buf.write("+)\3\2\2\2,\7\3\2\2\2-.\7m\2\2./\7\5\2\2/\60\5\f\7\2\60")
        buf.write("\t\3\2\2\2\61\62\t\2\2\2\62\13\3\2\2\2\63\64\5\16\b\2")
        buf.write("\64\r\3\2\2\2\658\5\n\6\2\668\7m\2\2\67\65\3\2\2\2\67")
        buf.write("\66\3\2\2\28@\3\2\2\29<\7\23\2\2:=\5\n\6\2;=\7m\2\2<:")
        buf.write("\3\2\2\2<;\3\2\2\2=?\3\2\2\2>9\3\2\2\2?B\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2A\17\3\2\2\2B@\3\2\2\2CD\7\6\2\2DG\7\"\2")
        buf.write("\2EH\5\n\6\2FH\7m\2\2GE\3\2\2\2GF\3\2\2\2HP\3\2\2\2IL")
        buf.write("\7(\2\2JM\5\n\6\2KM\7m\2\2LJ\3\2\2\2LK\3\2\2\2MO\3\2\2")
        buf.write("\2NI\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2R")
        buf.write("P\3\2\2\2ST\7#\2\2T\21\3\2\2\2UV\5\2\2\2V\23\3\2\2\2\f")
        buf.write("\27\34$+\67<@GLP")
        return buf.getvalue()


class milestone_2Parser ( Parser ):

    grammarFileName = "milestone_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'zar'", "'int'", "'='", "'echo'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'~'", "'&'", "'|'", "'<'", "'>'", "'@'", 
                     "'%'", "'!'", "'^'", "'.'", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'", "<INVALID>", "'and'", 
                     "'var'", "'addr'", "'as'", "'asm'", "'bind'", "'block'", 
                     "'break'", "'case'", "'cast'", "'concept'", "'const'", 
                     "'continue'", "'converter'", "'defer'", "'discard'", 
                     "'distinct'", "'div'", "'do'", "'elif'", "'else'", 
                     "'end'", "'enum'", "'except'", "'export'", "'finally'", 
                     "'for'", "'from'", "'func'", "'if'", "'import'", "'in'", 
                     "'include'", "'interface'", "'is'", "'isnot'", "'iterator'", 
                     "'let'", "'macro'", "'method'", "'mixin'", "'mod'", 
                     "'nil'", "'not'", "'notin'", "'object'", "'of'", "'or'", 
                     "'out'", "'proc'", "'ptr'", "'raise'", "'ref'", "'return'", 
                     "'shl'", "'shr'", "'static'", "'template'", "'try'", 
                     "'tuple'", "'type'", "'using'", "'when'", "'while'", 
                     "'xor'", "'yield'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INDENT", "SPACE", "MULTILINECOMMENT", 
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
    RULE_varStmt = 2
    RULE_assignStmt = 3
    RULE_literal = 4
    RULE_expr = 5
    RULE_simpleExpr = 6
    RULE_echoStmt = 7
    RULE_start = 8

    ruleNames =  [ "module", "stmt", "varStmt", "assignStmt", "literal", 
                   "expr", "simpleExpr", "echoStmt", "start" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INDENT=5
    SPACE=6
    MULTILINECOMMENT=7
    MULTILINEDOCUMENTATION=8
    COMMENT=9
    TRIPLESTR_LIT=10
    STR_LIT=11
    CHAR_LIT=12
    RSTR_LIT=13
    GENERALIZED_STR_LIT=14
    GENERALIZED_TRIPLESTR_LIT=15
    EQUALS_OPERATOR=16
    ADD_OPERATOR=17
    MUL_OPERATOR=18
    MINUS_OPERATOR=19
    DIV_OPERATOR=20
    BITWISE_NOT_OPERATOR=21
    AND_OPERATOR=22
    OR_OPERATOR=23
    LESS_THAN=24
    GREATER_THAN=25
    AT=26
    MODULUS=27
    NOT_OPERATOR=28
    XOR_OPERATOR=29
    DOT=30
    COLON=31
    OPEN_PAREN=32
    CLOSE_PAREN=33
    OPEN_BRACE=34
    CLOSE_BRACE=35
    OPEN_BRACK=36
    CLOSE_BRACK=37
    COMMA=38
    SEMI_COLON=39
    KEYW=40
    AND=41
    VARIABLE=42
    ADDR=43
    AS=44
    ASM=45
    BIND=46
    BLOCK=47
    BREAK=48
    CASE=49
    CAST=50
    CONCEPT=51
    CONST=52
    CONTINUE=53
    CONVERTER=54
    DEFER=55
    DISCARD=56
    DISTINCT=57
    DIV=58
    DO=59
    ELIF=60
    ELSE=61
    END=62
    ENUM=63
    EXCEPT=64
    EXPORT=65
    FINALLY=66
    FOR=67
    FROM=68
    FUNC=69
    IF=70
    IMPORT=71
    IN=72
    INCLUDE=73
    INTERFACE=74
    IS=75
    ISNOT=76
    ITERATOR=77
    LET=78
    MACRO=79
    METHOD=80
    MIXIN=81
    MOD=82
    NIL=83
    NOT=84
    NOTIN=85
    OBJECT=86
    OF=87
    OR=88
    OUT=89
    PROC=90
    PTR=91
    RAISE=92
    REF=93
    RETURN=94
    SHL=95
    SHR=96
    STATIC=97
    TEMPLATE=98
    TRY=99
    TUPLE=100
    TYPE=101
    USING=102
    WHEN=103
    WHILE=104
    XOR=105
    YIELD=106
    IDENTIFIER=107
    DIGIT=108
    LETTER=109
    INT_LIT=110
    HEXDIGIT=111
    OCTDIGIT=112
    BINDIGIT=113
    HEX_LIT=114
    DEC_LIT=115
    OCT_LIT=116
    BIN_LIT=117
    INT8_LIT=118
    INT16_LIT=119
    INT32_LIT=120
    INT64_LIT=121
    UINT_LIT=122
    UINT8_LIT=123
    UINT16_LIT=124
    UINT32_LIT=125
    UINT64_LIT=126
    EXP=127
    FLOAT_LIT=128
    FLOAT32_SUFFIX=129
    FLOAT32_LIT=130
    FLOAT64_SUFFIX=131
    FLOAT64_LIT=132

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ModuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(milestone_2Parser.StmtContext)
            else:
                return self.getTypedRuleContext(milestone_2Parser.StmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stmt()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==milestone_2Parser.T__0 or _la==milestone_2Parser.T__3 or _la==milestone_2Parser.IDENTIFIER):
                    break

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

        def varStmt(self):
            return self.getTypedRuleContext(milestone_2Parser.VarStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(milestone_2Parser.AssignStmtContext,0)


        def echoStmt(self):
            return self.getTypedRuleContext(milestone_2Parser.EchoStmtContext,0)


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
            self.state = 26
            token = self._input.LA(1)
            if token in [milestone_2Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.varStmt()

            elif token in [milestone_2Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assignStmt()

            elif token in [milestone_2Parser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.echoStmt()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.IDENTIFIER)
            else:
                return self.getToken(milestone_2Parser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.COMMA)
            else:
                return self.getToken(milestone_2Parser.COMMA, i)

        def COLON(self):
            return self.getToken(milestone_2Parser.COLON, 0)

        def literal(self):
            return self.getTypedRuleContext(milestone_2Parser.LiteralContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_varStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarStmt" ):
                listener.enterVarStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarStmt" ):
                listener.exitVarStmt(self)




    def varStmt(self):

        localctx = milestone_2Parser.VarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(milestone_2Parser.T__0)
            self.state = 29
            self.match(milestone_2Parser.IDENTIFIER)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==milestone_2Parser.COMMA:
                self.state = 30
                self.match(milestone_2Parser.COMMA)
                self.state = 31
                self.match(milestone_2Parser.IDENTIFIER)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            token = self._input.LA(1)
            if token in [milestone_2Parser.COLON]:
                self.state = 37
                self.match(milestone_2Parser.COLON)
                self.state = 38
                self.match(milestone_2Parser.T__1)

            elif token in [milestone_2Parser.T__2]:
                self.state = 39
                self.match(milestone_2Parser.T__2)
                self.state = 40
                self.literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(milestone_2Parser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(milestone_2Parser.ExprContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)




    def assignStmt(self):

        localctx = milestone_2Parser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(milestone_2Parser.IDENTIFIER)
            self.state = 44
            self.match(milestone_2Parser.T__2)
            self.state = 45
            self.expr()
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
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_2Parser.TRIPLESTR_LIT) | (1 << milestone_2Parser.STR_LIT) | (1 << milestone_2Parser.CHAR_LIT) | (1 << milestone_2Parser.RSTR_LIT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (milestone_2Parser.NIL - 83)) | (1 << (milestone_2Parser.INT_LIT - 83)) | (1 << (milestone_2Parser.INT8_LIT - 83)) | (1 << (milestone_2Parser.INT16_LIT - 83)) | (1 << (milestone_2Parser.INT32_LIT - 83)) | (1 << (milestone_2Parser.INT64_LIT - 83)) | (1 << (milestone_2Parser.UINT_LIT - 83)) | (1 << (milestone_2Parser.UINT8_LIT - 83)) | (1 << (milestone_2Parser.UINT16_LIT - 83)) | (1 << (milestone_2Parser.UINT32_LIT - 83)) | (1 << (milestone_2Parser.UINT64_LIT - 83)) | (1 << (milestone_2Parser.FLOAT_LIT - 83)) | (1 << (milestone_2Parser.FLOAT32_LIT - 83)) | (1 << (milestone_2Parser.FLOAT64_LIT - 83)))) != 0)):
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

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpr(self):
            return self.getTypedRuleContext(milestone_2Parser.SimpleExprContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = milestone_2Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.simpleExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpleExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(milestone_2Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(milestone_2Parser.LiteralContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.IDENTIFIER)
            else:
                return self.getToken(milestone_2Parser.IDENTIFIER, i)

        def getRuleIndex(self):
            return milestone_2Parser.RULE_simpleExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpr" ):
                listener.enterSimpleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpr" ):
                listener.exitSimpleExpr(self)




    def simpleExpr(self):

        localctx = milestone_2Parser.SimpleExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simpleExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            token = self._input.LA(1)
            if token in [milestone_2Parser.TRIPLESTR_LIT, milestone_2Parser.STR_LIT, milestone_2Parser.CHAR_LIT, milestone_2Parser.RSTR_LIT, milestone_2Parser.NIL, milestone_2Parser.INT_LIT, milestone_2Parser.INT8_LIT, milestone_2Parser.INT16_LIT, milestone_2Parser.INT32_LIT, milestone_2Parser.INT64_LIT, milestone_2Parser.UINT_LIT, milestone_2Parser.UINT8_LIT, milestone_2Parser.UINT16_LIT, milestone_2Parser.UINT32_LIT, milestone_2Parser.UINT64_LIT, milestone_2Parser.FLOAT_LIT, milestone_2Parser.FLOAT32_LIT, milestone_2Parser.FLOAT64_LIT]:
                self.state = 51
                self.literal()

            elif token in [milestone_2Parser.IDENTIFIER]:
                self.state = 52
                self.match(milestone_2Parser.IDENTIFIER)

            else:
                raise NoViableAltException(self)

            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==milestone_2Parser.ADD_OPERATOR:
                self.state = 55
                self.match(milestone_2Parser.ADD_OPERATOR)
                self.state = 58
                token = self._input.LA(1)
                if token in [milestone_2Parser.TRIPLESTR_LIT, milestone_2Parser.STR_LIT, milestone_2Parser.CHAR_LIT, milestone_2Parser.RSTR_LIT, milestone_2Parser.NIL, milestone_2Parser.INT_LIT, milestone_2Parser.INT8_LIT, milestone_2Parser.INT16_LIT, milestone_2Parser.INT32_LIT, milestone_2Parser.INT64_LIT, milestone_2Parser.UINT_LIT, milestone_2Parser.UINT8_LIT, milestone_2Parser.UINT16_LIT, milestone_2Parser.UINT32_LIT, milestone_2Parser.UINT64_LIT, milestone_2Parser.FLOAT_LIT, milestone_2Parser.FLOAT32_LIT, milestone_2Parser.FLOAT64_LIT]:
                    self.state = 56
                    self.literal()

                elif token in [milestone_2Parser.IDENTIFIER]:
                    self.state = 57
                    self.match(milestone_2Parser.IDENTIFIER)

                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EchoStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(milestone_2Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(milestone_2Parser.LiteralContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.IDENTIFIER)
            else:
                return self.getToken(milestone_2Parser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.COMMA)
            else:
                return self.getToken(milestone_2Parser.COMMA, i)

        def getRuleIndex(self):
            return milestone_2Parser.RULE_echoStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEchoStmt" ):
                listener.enterEchoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEchoStmt" ):
                listener.exitEchoStmt(self)




    def echoStmt(self):

        localctx = milestone_2Parser.EchoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_echoStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(milestone_2Parser.T__3)
            self.state = 66
            self.match(milestone_2Parser.OPEN_PAREN)
            self.state = 69
            token = self._input.LA(1)
            if token in [milestone_2Parser.TRIPLESTR_LIT, milestone_2Parser.STR_LIT, milestone_2Parser.CHAR_LIT, milestone_2Parser.RSTR_LIT, milestone_2Parser.NIL, milestone_2Parser.INT_LIT, milestone_2Parser.INT8_LIT, milestone_2Parser.INT16_LIT, milestone_2Parser.INT32_LIT, milestone_2Parser.INT64_LIT, milestone_2Parser.UINT_LIT, milestone_2Parser.UINT8_LIT, milestone_2Parser.UINT16_LIT, milestone_2Parser.UINT32_LIT, milestone_2Parser.UINT64_LIT, milestone_2Parser.FLOAT_LIT, milestone_2Parser.FLOAT32_LIT, milestone_2Parser.FLOAT64_LIT]:
                self.state = 67
                self.literal()

            elif token in [milestone_2Parser.IDENTIFIER]:
                self.state = 68
                self.match(milestone_2Parser.IDENTIFIER)

            else:
                raise NoViableAltException(self)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==milestone_2Parser.COMMA:
                self.state = 71
                self.match(milestone_2Parser.COMMA)
                self.state = 74
                token = self._input.LA(1)
                if token in [milestone_2Parser.TRIPLESTR_LIT, milestone_2Parser.STR_LIT, milestone_2Parser.CHAR_LIT, milestone_2Parser.RSTR_LIT, milestone_2Parser.NIL, milestone_2Parser.INT_LIT, milestone_2Parser.INT8_LIT, milestone_2Parser.INT16_LIT, milestone_2Parser.INT32_LIT, milestone_2Parser.INT64_LIT, milestone_2Parser.UINT_LIT, milestone_2Parser.UINT8_LIT, milestone_2Parser.UINT16_LIT, milestone_2Parser.UINT32_LIT, milestone_2Parser.UINT64_LIT, milestone_2Parser.FLOAT_LIT, milestone_2Parser.FLOAT32_LIT, milestone_2Parser.FLOAT64_LIT]:
                    self.state = 72
                    self.literal()

                elif token in [milestone_2Parser.IDENTIFIER]:
                    self.state = 73
                    self.match(milestone_2Parser.IDENTIFIER)

                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(milestone_2Parser.CLOSE_PAREN)
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
        self.enterRule(localctx, 16, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.module()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





