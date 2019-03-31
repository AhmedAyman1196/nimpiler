// Generated from milestone_1.g4 by ANTLR 4.5.3
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class milestone_1Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SPACE=1, INDENTATION=2, MULTILINECOMMENT=3, COMMENT=4, TRIPLESTR_LIT=5, 
		STR_LIT=6, CHAR_LIT=7, TRIPLESTR_ITEM=8, RSTR_LIT=9, GENERALIZED_STR_LIT=10, 
		GENERALIZED_TRIPLESTR_LIT=11, EQUALS_OPERATOR=12, ADD_OPERATOR=13, MUL_OPERATOR=14, 
		MINUS_OPERATOR=15, DIV_OPERATOR=16, BITWISE_NOT_OPERATOR=17, AND_OPERATOR=18, 
		OR_OPERATOR=19, LESS_THAN=20, GREATER_THAN=21, AT=22, MODULUS=23, NOT_OPERATOR=24, 
		XOR_OPERATOR=25, DOT=26, COLON=27, OPEN_PAREN=28, CLOSE_PAREN=29, OPEN_BRACE=30, 
		CLOSE_BRACE=31, OPEN_BRACK=32, CLOSE_BRACK=33, COMMA=34, SEMI_COLON=35, 
		AND=36, VARIABLE=37, ADDR=38, AS=39, ASM=40, BIND=41, BLOCK=42, BREAK=43, 
		CASE=44, CAST=45, CONCEPT=46, CONST=47, CONTINUE=48, CONVERTER=49, DEFER=50, 
		DISCARD=51, DISTINCT=52, DIV=53, DO=54, ELIF=55, ELSE=56, END=57, ENUM=58, 
		EXCEPT=59, EXPORT=60, FINALLY=61, FOR=62, FROM=63, FUNC=64, IF=65, IMPORT=66, 
		IN=67, INCLUDE=68, INTERFACE=69, IS=70, ISNOT=71, ITERATOR=72, LET=73, 
		MACRO=74, METHOD=75, MIXIN=76, MOD=77, NIL=78, NOT=79, NOTIN=80, OBJECT=81, 
		OF=82, OR=83, OUT=84, PROC=85, PTR=86, RAISE=87, REF=88, RETURN=89, SHL=90, 
		SHR=91, STATIC=92, TEMPLATE=93, TRY=94, TUPLE=95, TYPE=96, USING=97, WHEN=98, 
		WHILE=99, XOR=100, YIELD=101, IDENTIFIER=102, DIGIT=103, LETTER=104, HEXDIGIT=105, 
		OCTDIGIT=106, BINDIGIT=107, HEX_LIT=108, DEC_LIT=109, OCT_LIT=110, BIN_LIT=111, 
		INT_LIT=112, INT8_LIT=113, INT16_LIT=114, INT32_LIT=115, INT64_LIT=116, 
		UINT_LIT=117, UINT8_LIT=118, UINT16_LIT=119, UINT32_LIT=120, UINT64_LIT=121, 
		EXP=122, FLOAT_LIT=123, FLOAT32_SUFFIX=124, FLOAT32_LIT=125, FLOAT64_SUFFIX=126, 
		FLOAT64_LIT=127;
	public static final int
		RULE_start = 0;
	public static final String[] ruleNames = {
		"start"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, "'    '", null, null, null, null, null, "'x'", null, null, 
		null, "'='", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", "'|'", "'<'", "'>'", 
		"'@'", "'%'", "'!'", "'^'", "'.'", "':'", "'('", "')'", "'{'", "'}'", 
		"'['", "']'", "','", "';'", "'and'", "'var'", "'addr'", "'as'", "'asm'", 
		"'bind'", "'block'", "'break'", "'case'", "'cast'", "'concept'", "'const'", 
		"'continue'", "'converter'", "'defer'", "'discard'", "'distinct'", "'div'", 
		"'do'", "'elif'", "'else'", "'end'", "'enum'", "'except'", "'export'", 
		"'finally'", "'for'", "'from'", "'func'", "'if'", "'import'", "'in'", 
		"'include'", "'interface'", "'is'", "'isnot'", "'iterator'", "'let'", 
		"'macro'", "'method'", "'mixin'", "'mod'", "'nil'", "'not'", "'notin'", 
		"'object'", "'of'", "'or'", "'out'", "'proc'", "'ptr'", "'raise'", "'ref'", 
		"'return'", "'shl'", "'shr'", "'static'", "'template'", "'try'", "'tuple'", 
		"'type'", "'using'", "'when'", "'while'", "'xor'", "'yield'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "SPACE", "INDENTATION", "MULTILINECOMMENT", "COMMENT", "TRIPLESTR_LIT", 
		"STR_LIT", "CHAR_LIT", "TRIPLESTR_ITEM", "RSTR_LIT", "GENERALIZED_STR_LIT", 
		"GENERALIZED_TRIPLESTR_LIT", "EQUALS_OPERATOR", "ADD_OPERATOR", "MUL_OPERATOR", 
		"MINUS_OPERATOR", "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
		"OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", "MODULUS", "NOT_OPERATOR", 
		"XOR_OPERATOR", "DOT", "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
		"CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", "SEMI_COLON", "AND", 
		"VARIABLE", "ADDR", "AS", "ASM", "BIND", "BLOCK", "BREAK", "CASE", "CAST", 
		"CONCEPT", "CONST", "CONTINUE", "CONVERTER", "DEFER", "DISCARD", "DISTINCT", 
		"DIV", "DO", "ELIF", "ELSE", "END", "ENUM", "EXCEPT", "EXPORT", "FINALLY", 
		"FOR", "FROM", "FUNC", "IF", "IMPORT", "IN", "INCLUDE", "INTERFACE", "IS", 
		"ISNOT", "ITERATOR", "LET", "MACRO", "METHOD", "MIXIN", "MOD", "NIL", 
		"NOT", "NOTIN", "OBJECT", "OF", "OR", "OUT", "PROC", "PTR", "RAISE", "REF", 
		"RETURN", "SHL", "SHR", "STATIC", "TEMPLATE", "TRY", "TUPLE", "TYPE", 
		"USING", "WHEN", "WHILE", "XOR", "YIELD", "IDENTIFIER", "DIGIT", "LETTER", 
		"HEXDIGIT", "OCTDIGIT", "BINDIGIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", "BIN_LIT", 
		"INT_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", "UINT_LIT", 
		"UINT8_LIT", "UINT16_LIT", "UINT32_LIT", "UINT64_LIT", "EXP", "FLOAT_LIT", 
		"FLOAT32_SUFFIX", "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "milestone_1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public milestone_1Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StartContext extends ParserRuleContext {
		public TerminalNode SPACE() { return getToken(milestone_1Parser.SPACE, 0); }
		public TerminalNode AND() { return getToken(milestone_1Parser.AND, 0); }
		public TerminalNode VARIABLE() { return getToken(milestone_1Parser.VARIABLE, 0); }
		public TerminalNode ADDR() { return getToken(milestone_1Parser.ADDR, 0); }
		public TerminalNode AS() { return getToken(milestone_1Parser.AS, 0); }
		public TerminalNode ASM() { return getToken(milestone_1Parser.ASM, 0); }
		public TerminalNode BIND() { return getToken(milestone_1Parser.BIND, 0); }
		public TerminalNode BLOCK() { return getToken(milestone_1Parser.BLOCK, 0); }
		public TerminalNode BREAK() { return getToken(milestone_1Parser.BREAK, 0); }
		public TerminalNode CASE() { return getToken(milestone_1Parser.CASE, 0); }
		public TerminalNode CAST() { return getToken(milestone_1Parser.CAST, 0); }
		public TerminalNode CONCEPT() { return getToken(milestone_1Parser.CONCEPT, 0); }
		public TerminalNode CONST() { return getToken(milestone_1Parser.CONST, 0); }
		public TerminalNode CONTINUE() { return getToken(milestone_1Parser.CONTINUE, 0); }
		public TerminalNode CONVERTER() { return getToken(milestone_1Parser.CONVERTER, 0); }
		public TerminalNode DEFER() { return getToken(milestone_1Parser.DEFER, 0); }
		public TerminalNode DISCARD() { return getToken(milestone_1Parser.DISCARD, 0); }
		public TerminalNode DISTINCT() { return getToken(milestone_1Parser.DISTINCT, 0); }
		public TerminalNode DIV() { return getToken(milestone_1Parser.DIV, 0); }
		public TerminalNode DO() { return getToken(milestone_1Parser.DO, 0); }
		public TerminalNode ELIF() { return getToken(milestone_1Parser.ELIF, 0); }
		public TerminalNode ELSE() { return getToken(milestone_1Parser.ELSE, 0); }
		public TerminalNode END() { return getToken(milestone_1Parser.END, 0); }
		public TerminalNode ENUM() { return getToken(milestone_1Parser.ENUM, 0); }
		public TerminalNode EXCEPT() { return getToken(milestone_1Parser.EXCEPT, 0); }
		public TerminalNode EXPORT() { return getToken(milestone_1Parser.EXPORT, 0); }
		public TerminalNode FINALLY() { return getToken(milestone_1Parser.FINALLY, 0); }
		public TerminalNode FOR() { return getToken(milestone_1Parser.FOR, 0); }
		public TerminalNode FROM() { return getToken(milestone_1Parser.FROM, 0); }
		public TerminalNode FUNC() { return getToken(milestone_1Parser.FUNC, 0); }
		public TerminalNode IF() { return getToken(milestone_1Parser.IF, 0); }
		public TerminalNode IMPORT() { return getToken(milestone_1Parser.IMPORT, 0); }
		public TerminalNode IN() { return getToken(milestone_1Parser.IN, 0); }
		public TerminalNode INCLUDE() { return getToken(milestone_1Parser.INCLUDE, 0); }
		public TerminalNode INTERFACE() { return getToken(milestone_1Parser.INTERFACE, 0); }
		public TerminalNode IS() { return getToken(milestone_1Parser.IS, 0); }
		public TerminalNode ISNOT() { return getToken(milestone_1Parser.ISNOT, 0); }
		public TerminalNode ITERATOR() { return getToken(milestone_1Parser.ITERATOR, 0); }
		public TerminalNode LET() { return getToken(milestone_1Parser.LET, 0); }
		public TerminalNode MACRO() { return getToken(milestone_1Parser.MACRO, 0); }
		public TerminalNode METHOD() { return getToken(milestone_1Parser.METHOD, 0); }
		public TerminalNode MIXIN() { return getToken(milestone_1Parser.MIXIN, 0); }
		public TerminalNode MOD() { return getToken(milestone_1Parser.MOD, 0); }
		public TerminalNode NIL() { return getToken(milestone_1Parser.NIL, 0); }
		public TerminalNode NOT() { return getToken(milestone_1Parser.NOT, 0); }
		public TerminalNode NOTIN() { return getToken(milestone_1Parser.NOTIN, 0); }
		public TerminalNode OBJECT() { return getToken(milestone_1Parser.OBJECT, 0); }
		public TerminalNode OF() { return getToken(milestone_1Parser.OF, 0); }
		public TerminalNode OR() { return getToken(milestone_1Parser.OR, 0); }
		public TerminalNode OUT() { return getToken(milestone_1Parser.OUT, 0); }
		public TerminalNode PROC() { return getToken(milestone_1Parser.PROC, 0); }
		public TerminalNode PTR() { return getToken(milestone_1Parser.PTR, 0); }
		public TerminalNode RAISE() { return getToken(milestone_1Parser.RAISE, 0); }
		public TerminalNode REF() { return getToken(milestone_1Parser.REF, 0); }
		public TerminalNode RETURN() { return getToken(milestone_1Parser.RETURN, 0); }
		public TerminalNode SHL() { return getToken(milestone_1Parser.SHL, 0); }
		public TerminalNode SHR() { return getToken(milestone_1Parser.SHR, 0); }
		public TerminalNode STATIC() { return getToken(milestone_1Parser.STATIC, 0); }
		public TerminalNode TEMPLATE() { return getToken(milestone_1Parser.TEMPLATE, 0); }
		public TerminalNode TRY() { return getToken(milestone_1Parser.TRY, 0); }
		public TerminalNode TUPLE() { return getToken(milestone_1Parser.TUPLE, 0); }
		public TerminalNode TYPE() { return getToken(milestone_1Parser.TYPE, 0); }
		public TerminalNode USING() { return getToken(milestone_1Parser.USING, 0); }
		public TerminalNode WHEN() { return getToken(milestone_1Parser.WHEN, 0); }
		public TerminalNode WHILE() { return getToken(milestone_1Parser.WHILE, 0); }
		public TerminalNode XOR() { return getToken(milestone_1Parser.XOR, 0); }
		public TerminalNode YIELD() { return getToken(milestone_1Parser.YIELD, 0); }
		public TerminalNode TRIPLESTR_LIT() { return getToken(milestone_1Parser.TRIPLESTR_LIT, 0); }
		public TerminalNode STR_LIT() { return getToken(milestone_1Parser.STR_LIT, 0); }
		public TerminalNode CHAR_LIT() { return getToken(milestone_1Parser.CHAR_LIT, 0); }
		public TerminalNode TRIPLESTR_ITEM() { return getToken(milestone_1Parser.TRIPLESTR_ITEM, 0); }
		public TerminalNode RSTR_LIT() { return getToken(milestone_1Parser.RSTR_LIT, 0); }
		public TerminalNode GENERALIZED_STR_LIT() { return getToken(milestone_1Parser.GENERALIZED_STR_LIT, 0); }
		public TerminalNode GENERALIZED_TRIPLESTR_LIT() { return getToken(milestone_1Parser.GENERALIZED_TRIPLESTR_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(milestone_1Parser.IDENTIFIER, 0); }
		public TerminalNode LETTER() { return getToken(milestone_1Parser.LETTER, 0); }
		public List<TerminalNode> COMMA() { return getTokens(milestone_1Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(milestone_1Parser.COMMA, i);
		}
		public TerminalNode DIGIT() { return getToken(milestone_1Parser.DIGIT, 0); }
		public TerminalNode EQUALS_OPERATOR() { return getToken(milestone_1Parser.EQUALS_OPERATOR, 0); }
		public TerminalNode ADD_OPERATOR() { return getToken(milestone_1Parser.ADD_OPERATOR, 0); }
		public TerminalNode MUL_OPERATOR() { return getToken(milestone_1Parser.MUL_OPERATOR, 0); }
		public TerminalNode MINUS_OPERATOR() { return getToken(milestone_1Parser.MINUS_OPERATOR, 0); }
		public TerminalNode DIV_OPERATOR() { return getToken(milestone_1Parser.DIV_OPERATOR, 0); }
		public TerminalNode BITWISE_NOT_OPERATOR() { return getToken(milestone_1Parser.BITWISE_NOT_OPERATOR, 0); }
		public TerminalNode AND_OPERATOR() { return getToken(milestone_1Parser.AND_OPERATOR, 0); }
		public TerminalNode OR_OPERATOR() { return getToken(milestone_1Parser.OR_OPERATOR, 0); }
		public TerminalNode LESS_THAN() { return getToken(milestone_1Parser.LESS_THAN, 0); }
		public TerminalNode GREATER_THAN() { return getToken(milestone_1Parser.GREATER_THAN, 0); }
		public TerminalNode AT() { return getToken(milestone_1Parser.AT, 0); }
		public TerminalNode MODULUS() { return getToken(milestone_1Parser.MODULUS, 0); }
		public TerminalNode NOT_OPERATOR() { return getToken(milestone_1Parser.NOT_OPERATOR, 0); }
		public TerminalNode XOR_OPERATOR() { return getToken(milestone_1Parser.XOR_OPERATOR, 0); }
		public TerminalNode DOT() { return getToken(milestone_1Parser.DOT, 0); }
		public TerminalNode COLON() { return getToken(milestone_1Parser.COLON, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(milestone_1Parser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(milestone_1Parser.CLOSE_PAREN, 0); }
		public TerminalNode OPEN_BRACE() { return getToken(milestone_1Parser.OPEN_BRACE, 0); }
		public TerminalNode CLOSE_BRACE() { return getToken(milestone_1Parser.CLOSE_BRACE, 0); }
		public TerminalNode OPEN_BRACK() { return getToken(milestone_1Parser.OPEN_BRACK, 0); }
		public TerminalNode CLOSE_BRACK() { return getToken(milestone_1Parser.CLOSE_BRACK, 0); }
		public TerminalNode SEMI_COLON() { return getToken(milestone_1Parser.SEMI_COLON, 0); }
		public TerminalNode COMMENT() { return getToken(milestone_1Parser.COMMENT, 0); }
		public TerminalNode MULTILINECOMMENT() { return getToken(milestone_1Parser.MULTILINECOMMENT, 0); }
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof milestone_1Listener ) ((milestone_1Listener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof milestone_1Listener ) ((milestone_1Listener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SPACE) | (1L << MULTILINECOMMENT) | (1L << COMMENT) | (1L << TRIPLESTR_LIT) | (1L << STR_LIT) | (1L << CHAR_LIT) | (1L << TRIPLESTR_ITEM) | (1L << RSTR_LIT) | (1L << GENERALIZED_STR_LIT) | (1L << GENERALIZED_TRIPLESTR_LIT) | (1L << EQUALS_OPERATOR) | (1L << ADD_OPERATOR) | (1L << MUL_OPERATOR) | (1L << MINUS_OPERATOR) | (1L << DIV_OPERATOR) | (1L << BITWISE_NOT_OPERATOR) | (1L << AND_OPERATOR) | (1L << OR_OPERATOR) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << AT) | (1L << MODULUS) | (1L << NOT_OPERATOR) | (1L << XOR_OPERATOR) | (1L << DOT) | (1L << COLON) | (1L << OPEN_PAREN) | (1L << CLOSE_PAREN) | (1L << OPEN_BRACE) | (1L << CLOSE_BRACE) | (1L << OPEN_BRACK) | (1L << CLOSE_BRACK) | (1L << COMMA) | (1L << SEMI_COLON) | (1L << AND) | (1L << VARIABLE) | (1L << ADDR) | (1L << AS) | (1L << ASM) | (1L << BIND) | (1L << BLOCK) | (1L << BREAK) | (1L << CASE) | (1L << CAST) | (1L << CONCEPT) | (1L << CONST) | (1L << CONTINUE) | (1L << CONVERTER) | (1L << DEFER) | (1L << DISCARD) | (1L << DISTINCT) | (1L << DIV) | (1L << DO) | (1L << ELIF) | (1L << ELSE) | (1L << END) | (1L << ENUM) | (1L << EXCEPT) | (1L << EXPORT) | (1L << FINALLY) | (1L << FOR) | (1L << FROM))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (FUNC - 64)) | (1L << (IF - 64)) | (1L << (IMPORT - 64)) | (1L << (IN - 64)) | (1L << (INCLUDE - 64)) | (1L << (INTERFACE - 64)) | (1L << (IS - 64)) | (1L << (ISNOT - 64)) | (1L << (ITERATOR - 64)) | (1L << (LET - 64)) | (1L << (MACRO - 64)) | (1L << (METHOD - 64)) | (1L << (MIXIN - 64)) | (1L << (MOD - 64)) | (1L << (NIL - 64)) | (1L << (NOT - 64)) | (1L << (NOTIN - 64)) | (1L << (OBJECT - 64)) | (1L << (OF - 64)) | (1L << (OR - 64)) | (1L << (OUT - 64)) | (1L << (PROC - 64)) | (1L << (PTR - 64)) | (1L << (RAISE - 64)) | (1L << (REF - 64)) | (1L << (RETURN - 64)) | (1L << (SHL - 64)) | (1L << (SHR - 64)) | (1L << (STATIC - 64)) | (1L << (TEMPLATE - 64)) | (1L << (TRY - 64)) | (1L << (TUPLE - 64)) | (1L << (TYPE - 64)) | (1L << (USING - 64)) | (1L << (WHEN - 64)) | (1L << (WHILE - 64)) | (1L << (XOR - 64)) | (1L << (YIELD - 64)) | (1L << (IDENTIFIER - 64)) | (1L << (DIGIT - 64)) | (1L << (LETTER - 64)))) != 0)) ) {
			_errHandler.recoverInline(this);
			} else {
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0081\7\4\2\t\2\3"+
		"\2\3\2\3\2\2\2\3\2\2\3\4\2\3\3\5j\5\2\4\3\2\2\2\4\5\t\2\2\2\5\3\3\2\2"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}