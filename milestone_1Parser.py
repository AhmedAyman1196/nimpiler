# Generated from milestone_1.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0081")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\3\5\2\3in{}\u0081\5\2")
        buf.write("\4\3\2\2\2\4\5\t\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", 
                     "'|'", "'<'", "'>'", "'@'", "'%'", "'!'", "'^'", "'.'", 
                     "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'", "'and'", "'var'", "'addr'", "'as'", "'asm'", 
                     "'bind'", "'block'", "'break'", "'case'", "'cast'", 
                     "'concept'", "'const'", "'continue'", "'converter'", 
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

    symbolicNames = [ "<INVALID>", "SPACE", "INDENT", "MULTILINECOMMENT", 
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
                      "IDENTIFIER", "DIGIT", "LETTER", "HEXDIGIT", "OCTDIGIT", 
                      "BINDIGIT", "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", 
                      "BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    SPACE=1
    INDENT=2
    MULTILINECOMMENT=3
    MULTILINEDOCUMENTATION=4
    COMMENT=5
    TRIPLESTR_LIT=6
    STR_LIT=7
    CHAR_LIT=8
    RSTR_LIT=9
    GENERALIZED_STR_LIT=10
    GENERALIZED_TRIPLESTR_LIT=11
    EQUALS_OPERATOR=12
    ADD_OPERATOR=13
    MUL_OPERATOR=14
    MINUS_OPERATOR=15
    DIV_OPERATOR=16
    BITWISE_NOT_OPERATOR=17
    AND_OPERATOR=18
    OR_OPERATOR=19
    LESS_THAN=20
    GREATER_THAN=21
    AT=22
    MODULUS=23
    NOT_OPERATOR=24
    XOR_OPERATOR=25
    DOT=26
    COLON=27
    OPEN_PAREN=28
    CLOSE_PAREN=29
    OPEN_BRACE=30
    CLOSE_BRACE=31
    OPEN_BRACK=32
    CLOSE_BRACK=33
    COMMA=34
    SEMI_COLON=35
    AND=36
    VARIABLE=37
    ADDR=38
    AS=39
    ASM=40
    BIND=41
    BLOCK=42
    BREAK=43
    CASE=44
    CAST=45
    CONCEPT=46
    CONST=47
    CONTINUE=48
    CONVERTER=49
    DEFER=50
    DISCARD=51
    DISTINCT=52
    DIV=53
    DO=54
    ELIF=55
    ELSE=56
    END=57
    ENUM=58
    EXCEPT=59
    EXPORT=60
    FINALLY=61
    FOR=62
    FROM=63
    FUNC=64
    IF=65
    IMPORT=66
    IN=67
    INCLUDE=68
    INTERFACE=69
    IS=70
    ISNOT=71
    ITERATOR=72
    LET=73
    MACRO=74
    METHOD=75
    MIXIN=76
    MOD=77
    NIL=78
    NOT=79
    NOTIN=80
    OBJECT=81
    OF=82
    OR=83
    OUT=84
    PROC=85
    PTR=86
    RAISE=87
    REF=88
    RETURN=89
    SHL=90
    SHR=91
    STATIC=92
    TEMPLATE=93
    TRY=94
    TUPLE=95
    TYPE=96
    USING=97
    WHEN=98
    WHILE=99
    XOR=100
    YIELD=101
    IDENTIFIER=102
    DIGIT=103
    LETTER=104
    HEXDIGIT=105
    OCTDIGIT=106
    BINDIGIT=107
    INT_LIT=108
    HEX_LIT=109
    DEC_LIT=110
    OCT_LIT=111
    BIN_LIT=112
    INT8_LIT=113
    INT16_LIT=114
    INT32_LIT=115
    INT64_LIT=116
    UINT_LIT=117
    UINT8_LIT=118
    UINT16_LIT=119
    UINT32_LIT=120
    UINT64_LIT=121
    EXP=122
    FLOAT_LIT=123
    FLOAT32_SUFFIX=124
    FLOAT32_LIT=125
    FLOAT64_SUFFIX=126
    FLOAT64_LIT=127

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self):
            return self.getToken(milestone_1Parser.SPACE, 0)

        def INDENT(self):
            return self.getToken(milestone_1Parser.INDENT, 0)

        def MULTILINEDOCUMENTATION(self):
            return self.getToken(milestone_1Parser.MULTILINEDOCUMENTATION, 0)

        def AND(self):
            return self.getToken(milestone_1Parser.AND, 0)

        def VARIABLE(self):
            return self.getToken(milestone_1Parser.VARIABLE, 0)

        def ADDR(self):
            return self.getToken(milestone_1Parser.ADDR, 0)

        def AS(self):
            return self.getToken(milestone_1Parser.AS, 0)

        def ASM(self):
            return self.getToken(milestone_1Parser.ASM, 0)

        def BIND(self):
            return self.getToken(milestone_1Parser.BIND, 0)

        def BLOCK(self):
            return self.getToken(milestone_1Parser.BLOCK, 0)

        def BREAK(self):
            return self.getToken(milestone_1Parser.BREAK, 0)

        def CASE(self):
            return self.getToken(milestone_1Parser.CASE, 0)

        def CAST(self):
            return self.getToken(milestone_1Parser.CAST, 0)

        def CONCEPT(self):
            return self.getToken(milestone_1Parser.CONCEPT, 0)

        def CONST(self):
            return self.getToken(milestone_1Parser.CONST, 0)

        def CONTINUE(self):
            return self.getToken(milestone_1Parser.CONTINUE, 0)

        def CONVERTER(self):
            return self.getToken(milestone_1Parser.CONVERTER, 0)

        def DEFER(self):
            return self.getToken(milestone_1Parser.DEFER, 0)

        def DISCARD(self):
            return self.getToken(milestone_1Parser.DISCARD, 0)

        def DISTINCT(self):
            return self.getToken(milestone_1Parser.DISTINCT, 0)

        def DIV(self):
            return self.getToken(milestone_1Parser.DIV, 0)

        def DO(self):
            return self.getToken(milestone_1Parser.DO, 0)

        def ELIF(self):
            return self.getToken(milestone_1Parser.ELIF, 0)

        def ELSE(self):
            return self.getToken(milestone_1Parser.ELSE, 0)

        def END(self):
            return self.getToken(milestone_1Parser.END, 0)

        def ENUM(self):
            return self.getToken(milestone_1Parser.ENUM, 0)

        def EXCEPT(self):
            return self.getToken(milestone_1Parser.EXCEPT, 0)

        def EXPORT(self):
            return self.getToken(milestone_1Parser.EXPORT, 0)

        def FINALLY(self):
            return self.getToken(milestone_1Parser.FINALLY, 0)

        def FOR(self):
            return self.getToken(milestone_1Parser.FOR, 0)

        def FROM(self):
            return self.getToken(milestone_1Parser.FROM, 0)

        def FUNC(self):
            return self.getToken(milestone_1Parser.FUNC, 0)

        def IF(self):
            return self.getToken(milestone_1Parser.IF, 0)

        def IMPORT(self):
            return self.getToken(milestone_1Parser.IMPORT, 0)

        def IN(self):
            return self.getToken(milestone_1Parser.IN, 0)

        def INCLUDE(self):
            return self.getToken(milestone_1Parser.INCLUDE, 0)

        def INTERFACE(self):
            return self.getToken(milestone_1Parser.INTERFACE, 0)

        def IS(self):
            return self.getToken(milestone_1Parser.IS, 0)

        def ISNOT(self):
            return self.getToken(milestone_1Parser.ISNOT, 0)

        def ITERATOR(self):
            return self.getToken(milestone_1Parser.ITERATOR, 0)

        def LET(self):
            return self.getToken(milestone_1Parser.LET, 0)

        def MACRO(self):
            return self.getToken(milestone_1Parser.MACRO, 0)

        def METHOD(self):
            return self.getToken(milestone_1Parser.METHOD, 0)

        def MIXIN(self):
            return self.getToken(milestone_1Parser.MIXIN, 0)

        def MOD(self):
            return self.getToken(milestone_1Parser.MOD, 0)

        def NIL(self):
            return self.getToken(milestone_1Parser.NIL, 0)

        def NOT(self):
            return self.getToken(milestone_1Parser.NOT, 0)

        def NOTIN(self):
            return self.getToken(milestone_1Parser.NOTIN, 0)

        def OBJECT(self):
            return self.getToken(milestone_1Parser.OBJECT, 0)

        def OF(self):
            return self.getToken(milestone_1Parser.OF, 0)

        def OR(self):
            return self.getToken(milestone_1Parser.OR, 0)

        def OUT(self):
            return self.getToken(milestone_1Parser.OUT, 0)

        def PROC(self):
            return self.getToken(milestone_1Parser.PROC, 0)

        def PTR(self):
            return self.getToken(milestone_1Parser.PTR, 0)

        def RAISE(self):
            return self.getToken(milestone_1Parser.RAISE, 0)

        def REF(self):
            return self.getToken(milestone_1Parser.REF, 0)

        def RETURN(self):
            return self.getToken(milestone_1Parser.RETURN, 0)

        def SHL(self):
            return self.getToken(milestone_1Parser.SHL, 0)

        def SHR(self):
            return self.getToken(milestone_1Parser.SHR, 0)

        def STATIC(self):
            return self.getToken(milestone_1Parser.STATIC, 0)

        def TEMPLATE(self):
            return self.getToken(milestone_1Parser.TEMPLATE, 0)

        def TRY(self):
            return self.getToken(milestone_1Parser.TRY, 0)

        def TUPLE(self):
            return self.getToken(milestone_1Parser.TUPLE, 0)

        def TYPE(self):
            return self.getToken(milestone_1Parser.TYPE, 0)

        def USING(self):
            return self.getToken(milestone_1Parser.USING, 0)

        def WHEN(self):
            return self.getToken(milestone_1Parser.WHEN, 0)

        def WHILE(self):
            return self.getToken(milestone_1Parser.WHILE, 0)

        def XOR(self):
            return self.getToken(milestone_1Parser.XOR, 0)

        def YIELD(self):
            return self.getToken(milestone_1Parser.YIELD, 0)

        def TRIPLESTR_LIT(self):
            return self.getToken(milestone_1Parser.TRIPLESTR_LIT, 0)

        def STR_LIT(self):
            return self.getToken(milestone_1Parser.STR_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(milestone_1Parser.CHAR_LIT, 0)

        def RSTR_LIT(self):
            return self.getToken(milestone_1Parser.RSTR_LIT, 0)

        def GENERALIZED_STR_LIT(self):
            return self.getToken(milestone_1Parser.GENERALIZED_STR_LIT, 0)

        def GENERALIZED_TRIPLESTR_LIT(self):
            return self.getToken(milestone_1Parser.GENERALIZED_TRIPLESTR_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(milestone_1Parser.IDENTIFIER, 0)

        def EQUALS_OPERATOR(self):
            return self.getToken(milestone_1Parser.EQUALS_OPERATOR, 0)

        def ADD_OPERATOR(self):
            return self.getToken(milestone_1Parser.ADD_OPERATOR, 0)

        def MUL_OPERATOR(self):
            return self.getToken(milestone_1Parser.MUL_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(milestone_1Parser.MINUS_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(milestone_1Parser.DIV_OPERATOR, 0)

        def BITWISE_NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.BITWISE_NOT_OPERATOR, 0)

        def AND_OPERATOR(self):
            return self.getToken(milestone_1Parser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(milestone_1Parser.OR_OPERATOR, 0)

        def LESS_THAN(self):
            return self.getToken(milestone_1Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(milestone_1Parser.GREATER_THAN, 0)

        def AT(self):
            return self.getToken(milestone_1Parser.AT, 0)

        def MODULUS(self):
            return self.getToken(milestone_1Parser.MODULUS, 0)

        def NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.NOT_OPERATOR, 0)

        def XOR_OPERATOR(self):
            return self.getToken(milestone_1Parser.XOR_OPERATOR, 0)

        def DOT(self):
            return self.getToken(milestone_1Parser.DOT, 0)

        def COLON(self):
            return self.getToken(milestone_1Parser.COLON, 0)

        def OPEN_PAREN(self):
            return self.getToken(milestone_1Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(milestone_1Parser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(milestone_1Parser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACE, 0)

        def OPEN_BRACK(self):
            return self.getToken(milestone_1Parser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACK, 0)

        def COMMA(self):
            return self.getToken(milestone_1Parser.COMMA, 0)

        def SEMI_COLON(self):
            return self.getToken(milestone_1Parser.SEMI_COLON, 0)

        def COMMENT(self):
            return self.getToken(milestone_1Parser.COMMENT, 0)

        def MULTILINECOMMENT(self):
            return self.getToken(milestone_1Parser.MULTILINECOMMENT, 0)

        def INT_LIT(self):
            return self.getToken(milestone_1Parser.INT_LIT, 0)

        def INT8_LIT(self):
            return self.getToken(milestone_1Parser.INT8_LIT, 0)

        def INT16_LIT(self):
            return self.getToken(milestone_1Parser.INT16_LIT, 0)

        def INT32_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_1Parser.INT32_LIT)
            else:
                return self.getToken(milestone_1Parser.INT32_LIT, i)

        def INT64_LIT(self):
            return self.getToken(milestone_1Parser.INT64_LIT, 0)

        def UINT_LIT(self):
            return self.getToken(milestone_1Parser.UINT_LIT, 0)

        def UINT8_LIT(self):
            return self.getToken(milestone_1Parser.UINT8_LIT, 0)

        def UINT16_LIT(self):
            return self.getToken(milestone_1Parser.UINT16_LIT, 0)

        def UINT32_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_1Parser.UINT32_LIT)
            else:
                return self.getToken(milestone_1Parser.UINT32_LIT, i)

        def UINT64_LIT(self):
            return self.getToken(milestone_1Parser.UINT64_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(milestone_1Parser.HEX_LIT, 0)

        def DEC_LIT(self):
            return self.getToken(milestone_1Parser.DEC_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(milestone_1Parser.OCT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(milestone_1Parser.BIN_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT_LIT, 0)

        def FLOAT32_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT32_SUFFIX, 0)

        def FLOAT32_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT32_LIT, 0)

        def FLOAT64_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT64_SUFFIX, 0)

        def FLOAT64_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT64_LIT, 0)

        def DIGIT(self):
            return self.getToken(milestone_1Parser.DIGIT, 0)

        def getRuleIndex(self):
            return milestone_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = milestone_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_1Parser.SPACE) | (1 << milestone_1Parser.INDENT) | (1 << milestone_1Parser.MULTILINECOMMENT) | (1 << milestone_1Parser.MULTILINEDOCUMENTATION) | (1 << milestone_1Parser.COMMENT) | (1 << milestone_1Parser.TRIPLESTR_LIT) | (1 << milestone_1Parser.STR_LIT) | (1 << milestone_1Parser.CHAR_LIT) | (1 << milestone_1Parser.RSTR_LIT) | (1 << milestone_1Parser.GENERALIZED_STR_LIT) | (1 << milestone_1Parser.GENERALIZED_TRIPLESTR_LIT) | (1 << milestone_1Parser.EQUALS_OPERATOR) | (1 << milestone_1Parser.ADD_OPERATOR) | (1 << milestone_1Parser.MUL_OPERATOR) | (1 << milestone_1Parser.MINUS_OPERATOR) | (1 << milestone_1Parser.DIV_OPERATOR) | (1 << milestone_1Parser.BITWISE_NOT_OPERATOR) | (1 << milestone_1Parser.AND_OPERATOR) | (1 << milestone_1Parser.OR_OPERATOR) | (1 << milestone_1Parser.LESS_THAN) | (1 << milestone_1Parser.GREATER_THAN) | (1 << milestone_1Parser.AT) | (1 << milestone_1Parser.MODULUS) | (1 << milestone_1Parser.NOT_OPERATOR) | (1 << milestone_1Parser.XOR_OPERATOR) | (1 << milestone_1Parser.DOT) | (1 << milestone_1Parser.COLON) | (1 << milestone_1Parser.OPEN_PAREN) | (1 << milestone_1Parser.CLOSE_PAREN) | (1 << milestone_1Parser.OPEN_BRACE) | (1 << milestone_1Parser.CLOSE_BRACE) | (1 << milestone_1Parser.OPEN_BRACK) | (1 << milestone_1Parser.CLOSE_BRACK) | (1 << milestone_1Parser.COMMA) | (1 << milestone_1Parser.SEMI_COLON) | (1 << milestone_1Parser.AND) | (1 << milestone_1Parser.VARIABLE) | (1 << milestone_1Parser.ADDR) | (1 << milestone_1Parser.AS) | (1 << milestone_1Parser.ASM) | (1 << milestone_1Parser.BIND) | (1 << milestone_1Parser.BLOCK) | (1 << milestone_1Parser.BREAK) | (1 << milestone_1Parser.CASE) | (1 << milestone_1Parser.CAST) | (1 << milestone_1Parser.CONCEPT) | (1 << milestone_1Parser.CONST) | (1 << milestone_1Parser.CONTINUE) | (1 << milestone_1Parser.CONVERTER) | (1 << milestone_1Parser.DEFER) | (1 << milestone_1Parser.DISCARD) | (1 << milestone_1Parser.DISTINCT) | (1 << milestone_1Parser.DIV) | (1 << milestone_1Parser.DO) | (1 << milestone_1Parser.ELIF) | (1 << milestone_1Parser.ELSE) | (1 << milestone_1Parser.END) | (1 << milestone_1Parser.ENUM) | (1 << milestone_1Parser.EXCEPT) | (1 << milestone_1Parser.EXPORT) | (1 << milestone_1Parser.FINALLY) | (1 << milestone_1Parser.FOR) | (1 << milestone_1Parser.FROM))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (milestone_1Parser.FUNC - 64)) | (1 << (milestone_1Parser.IF - 64)) | (1 << (milestone_1Parser.IMPORT - 64)) | (1 << (milestone_1Parser.IN - 64)) | (1 << (milestone_1Parser.INCLUDE - 64)) | (1 << (milestone_1Parser.INTERFACE - 64)) | (1 << (milestone_1Parser.IS - 64)) | (1 << (milestone_1Parser.ISNOT - 64)) | (1 << (milestone_1Parser.ITERATOR - 64)) | (1 << (milestone_1Parser.LET - 64)) | (1 << (milestone_1Parser.MACRO - 64)) | (1 << (milestone_1Parser.METHOD - 64)) | (1 << (milestone_1Parser.MIXIN - 64)) | (1 << (milestone_1Parser.MOD - 64)) | (1 << (milestone_1Parser.NIL - 64)) | (1 << (milestone_1Parser.NOT - 64)) | (1 << (milestone_1Parser.NOTIN - 64)) | (1 << (milestone_1Parser.OBJECT - 64)) | (1 << (milestone_1Parser.OF - 64)) | (1 << (milestone_1Parser.OR - 64)) | (1 << (milestone_1Parser.OUT - 64)) | (1 << (milestone_1Parser.PROC - 64)) | (1 << (milestone_1Parser.PTR - 64)) | (1 << (milestone_1Parser.RAISE - 64)) | (1 << (milestone_1Parser.REF - 64)) | (1 << (milestone_1Parser.RETURN - 64)) | (1 << (milestone_1Parser.SHL - 64)) | (1 << (milestone_1Parser.SHR - 64)) | (1 << (milestone_1Parser.STATIC - 64)) | (1 << (milestone_1Parser.TEMPLATE - 64)) | (1 << (milestone_1Parser.TRY - 64)) | (1 << (milestone_1Parser.TUPLE - 64)) | (1 << (milestone_1Parser.TYPE - 64)) | (1 << (milestone_1Parser.USING - 64)) | (1 << (milestone_1Parser.WHEN - 64)) | (1 << (milestone_1Parser.WHILE - 64)) | (1 << (milestone_1Parser.XOR - 64)) | (1 << (milestone_1Parser.YIELD - 64)) | (1 << (milestone_1Parser.IDENTIFIER - 64)) | (1 << (milestone_1Parser.DIGIT - 64)) | (1 << (milestone_1Parser.INT_LIT - 64)) | (1 << (milestone_1Parser.HEX_LIT - 64)) | (1 << (milestone_1Parser.DEC_LIT - 64)) | (1 << (milestone_1Parser.OCT_LIT - 64)) | (1 << (milestone_1Parser.BIN_LIT - 64)) | (1 << (milestone_1Parser.INT8_LIT - 64)) | (1 << (milestone_1Parser.INT16_LIT - 64)) | (1 << (milestone_1Parser.INT32_LIT - 64)) | (1 << (milestone_1Parser.INT64_LIT - 64)) | (1 << (milestone_1Parser.UINT_LIT - 64)) | (1 << (milestone_1Parser.UINT8_LIT - 64)) | (1 << (milestone_1Parser.UINT16_LIT - 64)) | (1 << (milestone_1Parser.UINT32_LIT - 64)) | (1 << (milestone_1Parser.UINT64_LIT - 64)) | (1 << (milestone_1Parser.FLOAT_LIT - 64)) | (1 << (milestone_1Parser.FLOAT32_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT32_LIT - 64)) | (1 << (milestone_1Parser.FLOAT64_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT64_LIT - 64)))) != 0)):
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





