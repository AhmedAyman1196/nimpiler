grammar milestone_1;

INDENT: '    '+;
SPACE :[\t\r\n] -> skip;

MULTILINECOMMENT: INDENT? '#[' (.|[\r\n])*? ']#\n';
COMMENT : INDENT? '#' .*? [\n];
MULTILINEDOCUMENTATION: '##[' (.|[\r\n])*? ']##' -> skip;

TRIPLESTR_LIT: '"""' .*? '"""';
STR_LIT:'"' .*? '"' ; // matches escape characters
CHAR_LIT: '\'' .*? '\'';

RSTR_LIT: ('r'|'R') STR_LIT; // doesnt match escape characters
GENERALIZED_STR_LIT: IDENTIFIER'('RSTR_LIT')' | IDENTIFIER STR_LIT;
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER'('TRIPLESTR_LIT')' | IDENTIFIER TRIPLESTR_LIT;

// OPERATORS
EQUALS_OPERATOR : '=' | '==' ;
ADD_OPERATOR : '+' ;
MUL_OPERATOR : '*' ;
MINUS_OPERATOR : '-';
DIV_OPERATOR : '/' ;
BITWISE_NOT_OPERATOR : '~' ;
AND_OPERATOR : '&' ;
OR_OPERATOR : '|' ;
LESS_THAN : '<' ;
GREATER_THAN : '>' ;
AT : '@' ;
MODULUS : '%' ;
NOT_OPERATOR : '!';
XOR_OPERATOR : '^';
DOT : '.' ;
COLON : ':' ;
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')' ;
OPEN_BRACE : '{' ;
CLOSE_BRACE : '}' ;
OPEN_BRACK : '[';
CLOSE_BRACK :  ']';
COMMA : ',' ;
SEMI_COLON : ';';

// KEYWORDS
AND : 'and' ;
VARIABLE: 'var';
ADDR: 'addr' ;
AS : 'as' ;
ASM: 'asm';
BIND: 'bind' ;
BLOCK: 'block';
BREAK: 'break' ;
CASE: 'case' ;
CAST: 'cast';
CONCEPT : 'concept';
CONST:  'const';
CONTINUE: 'continue';
CONVERTER :  'converter';
DEFER : 'defer';
DISCARD : 'discard';
DISTINCT : 'distinct';
DIV : 'div';
DO : 'do';
ELIF: 'elif';
ELSE : 'else' ;
END : 'end' ;
ENUM : 'enum' ;
EXCEPT : 'except' ;
EXPORT : 'export' ;
FINALLY : 'finally' ;
FOR : 'for' ;
FROM : 'from' ;
FUNC : 'func' ;
IF : 'if' ;
IMPORT : 'import' ;
IN : 'in' ;
INCLUDE : 'include' ;
INTERFACE : 'interface' ;
IS : 'is' ;
ISNOT : 'isnot' ;
ITERATOR : 'iterator' ;
LET : 'let' ;
MACRO : 'macro' ;
METHOD : 'method' ;
MIXIN : 'mixin' ;
MOD : 'mod' ;
NIL : 'nil' ;
NOT : 'not' ;
NOTIN : 'notin' ;
OBJECT : 'object' ;
OF : 'of' ;
OR : 'or' ;
OUT : 'out' ;
PROC : 'proc' ;
PTR : 'ptr' ;
RAISE : 'raise' ;
REF : 'ref' ;
RETURN : 'return' ;
SHL : 'shl' ;
SHR : 'shr' ;
STATIC : 'static' ;
TEMPLATE : 'template' ;
TRY : 'try' ;
TUPLE : 'tuple' ;
TYPE : 'type' ;
USING : 'using' ;
WHEN : 'when' ;
WHILE : 'while' ;
XOR : 'xor' ;
YIELD : 'yield' ;

INT_LIT : HEX_LIT
        | DEC_LIT
        | OCT_LIT
        | BIN_LIT ;


//DEC_LIT : DIGIT ( ['_'] DIGIT )*;
DEC_LIT : DIGIT (DIGIT)*? ;

// IDENTIFIER : LETTER+ ('_'? (LETTER | DIGIT)*)*
IDENTIFIER : LETTER+ ('_'(LETTER | DIGIT))*?;
DIGIT : [0-9] ;
LETTER :[a-zA-Z];

// NUMERALS
HEXDIGIT : DIGIT | [A-F] | [a-f] ;
OCTDIGIT : [0-7] ;
BINDIGIT : [0-1] ;


INT_LIT : HEX_LIT
        | DEC_LIT
        | OCT_LIT
        | BIN_LIT ;

//HEX_LIT : '0' ('x' | 'X' ) HEXDIGIT ( ['_'] HEXDIGIT )*
HEX_LIT : '0' ('x' | 'X' ) HEXDIGIT+ ;
//DEC_LIT : DIGIT ( ['_'] DIGIT )*;
DEC_LIT : (DIGIT ( '_' DIGIT+ )*) | DIGIT+ ;
//OCT_LIT = '0' 'o' OCTDIGIT ( ['_'] OCTDIGIT )*
OCT_LIT : '0' 'o' OCTDIGIT+ ;
//BIN_LIT = '0' ('b' | 'B' ) BINDIGIT ( ['_'] BINDIGIT )*
BIN_LIT : '0' ('b' | 'B' ) BINDIGIT+ ;

//INT8_LIT = INT_LIT ['\''] ('i' | 'I') '8'
INT8_LIT : INT_LIT '\'' ('i' | 'I') '8' ;
INT16_LIT : INT_LIT '\'' ('i' | 'I') '16' ;
INT32_LIT : INT_LIT '\'' ('i' | 'I') '32' ;
INT64_LIT : INT_LIT '\'' ('i' | 'I') '64' ;

UINT_LIT : INT_LIT '\'' ('u' | 'U') ;
UINT8_LIT : INT_LIT '\'' ('u' | 'U') '8' ;
UINT16_LIT : INT_LIT '\'' ('u' | 'U') '16' ;
UINT32_LIT : INT_LIT '\'' ('u' | 'U') '32' ;
UINT64_LIT : INT_LIT '\'' ('u' | 'U') '64' ;

//EXP : ('e' | 'E' ) ['+' | '-'] DIGIT ( ['_'] DIGIT )*
EXP : ('e' | 'E' ) ('+' | '-') DIGIT+ ;
//FLOAT_LIT : DIGIT+ (('.' DIGIT ('_' DIGIT)* EXP) |DIGIT) ;
FLOAT_LIT : DIGIT+ ('.' DIGIT+ EXP?) ;
FLOAT32_SUFFIX : '\'' ('f' | 'F') '32' ;
FLOAT32_LIT : HEX_LIT+ FLOAT32_SUFFIX
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT)+ FLOAT32_SUFFIX ;
FLOAT64_SUFFIX : '\'' ( ('f' | 'F') '64' ) | 'd' | 'D' ;
FLOAT64_LIT : HEX_LIT+ FLOAT64_SUFFIX
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT|'_')+ FLOAT64_SUFFIX ;

start :

 SPACE | INDENT | MULTILINEDOCUMENTATION |

 AND |VARIABLE  |ADDR |AS |ASM |BIND |BLOCK |BREAK |CASE |CAST |CONCEPT |CONST |
 CONTINUE |CONVERTER |DEFER |DISCARD |DISTINCT |DIV |DO | ELIF|ELSE| END | ENUM|
 EXCEPT| EXPORT| FINALLY| FOR| FROM| FUNC| IF| IMPORT| IN| INCLUDE| INTERFACE|
 IS| ISNOT| ITERATOR| LET| MACRO| METHOD| MIXIN| MOD| NIL| NOT| NOTIN| OBJECT| OF| OR|
 OUT| PROC| PTR| RAISE| REF| RETURN| SHL| SHR| STATIC| TEMPLATE| TRY| TUPLE| TYPE| USING|
 WHEN| WHILE| XOR| YIELD |

 TRIPLESTR_LIT |STR_LIT | CHAR_LIT | RSTR_LIT |GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT |
 IDENTIFIER |

 EQUALS_OPERATOR | ADD_OPERATOR |MUL_OPERATOR | MINUS_OPERATOR | DIV_OPERATOR |
 BITWISE_NOT_OPERATOR |AND_OPERATOR|OR_OPERATOR | LESS_THAN | GREATER_THAN |
 AT | MODULUS | NOT_OPERATOR | XOR_OPERATOR | DOT | COLON | OPEN_PAREN |
 CLOSE_PAREN | OPEN_BRACE | CLOSE_BRACE | OPEN_BRACK | CLOSE_BRACK | COMMA | SEMI_COLON |

 COMMENT | MULTILINECOMMENT |



 INT_LIT | INT8_LIT |INT16_LIT | INT32_LIT | INT32_LIT |INT64_LIT |
 UINT_LIT | UINT8_LIT | UINT16_LIT | UINT32_LIT | UINT32_LIT | UINT64_LIT |
 HEX_LIT|  DEC_LIT | OCT_LIT | BIN_LIT |

 FLOAT_LIT | FLOAT32_SUFFIX | FLOAT32_LIT | FLOAT64_SUFFIX | FLOAT64_LIT  | DIGIT
 ;
