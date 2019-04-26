grammar milestone_2;

// ------------------------------ Grammar --------------------------------------

start : module EOF;

module : stmt ((';' | INDENT)? stmt)*;

stmt : symbol | blockStmt | ifStmt | breakStmt | whileStmt | invokeFunc | forStmt | importStmt | varStmt | assignStmt
       | constStmt | echoStmt | letStmt | assretStmt;

varStmt : simpleVarStmt | complexVarStmt ;
simpleVarStmt : 'var' (IDENTIFIER (',' complexIdentifier)* ':' ('int'|'string'))+ ;
complexVarStmt : 'var' assignStmt ;

assignStmt : complexIdentifier '=' expr;

letStmt : 'let' assignStmt+ ;

expr : arrayConstr | simpleExpr | compareExpr | invokeFunc ;

constStmt: 'const' assignStmt+ ;

compareExpr : identOrLiteral ('<' | '>') identOrLiteral;

assretStmt: 'assert' literal '==' literal ;

simpleExpr: (identOrLiteral | invokeFunc) ('+' (identOrLiteral | invokeFunc))*;

echoStmt: 'echo' (simpleEcho | complexEcho);
complexEcho : '(' echoParam (',' echoParam)* ')';
simpleEcho : echoParam (',' echoParam)* ;

echoParam : identOrLiteral | invokeFunc;

importStmt : 'import' optInd? complexIdentifier (',' complexIdentifier)*;
optInd : COMMENT? INDENT ;

arrayConstr : complexIdentifier '[' ('int' | 'string') ']()' ;

complexIdentifier : IDENTIFIER('.' IDENTIFIER)*;

forStmt : 'for' complexIdentifier (',' complexIdentifier)* 'in' (complexIdentifier | invokeFunc) colcom stmt ;

invokeFunc : (complexIdentifier '.')? IDENTIFIER '(' funcParam (',' funcParam)* ')';

funcParam : identOrLiteral | (identOrLiteral '=' identOrLiteral);

identOrLiteral : literal | complexIdentifier | symbol;
symbol : 'action' | 'actions' ;

whileStmt : 'while' expr colcom stmt ;

breakStmt : 'break' optInd? expr? ;

ifStmt : 'if' condStmt  ;

condStmt : expr colcom stmt COMMENT?
          (INDENT? 'elif' expr colcom stmt)*
          (INDENT? 'else' colcom stmt)? ;

blockStmt : 'block' IDENTIFIER? colcom stmt ;

colcom : ':' COMMENT? ;

literal : DIGIT | INT_LIT | INT8_LIT | INT16_LIT | INT32_LIT | INT64_LIT
          | UINT_LIT | UINT8_LIT | UINT16_LIT | UINT32_LIT | UINT64_LIT
          | FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT
          | STR_LIT | RSTR_LIT | TRIPLESTR_LIT
          | CHAR_LIT
          | 'nil' ;

// =============================================================================
// ============================ Lexical Analysis ===============================

INDENT : ('    ')+ -> skip; // added this

SPACE :(' '| [\t\r\n]) -> skip;

MULTILINECOMMENT: '#[' ((.|[\r\n]) | COMMENT | MULTILINECOMMENT )*']#' -> skip;
MULTILINEDOCUMENTATION: '##[' (.|[\r\n])*? ']##' -> skip;

COMMENT : '#' .*? [\n]  -> skip ;

TRIPLESTR_LIT: '"""' .*? '"""';
STR_LIT:'"' .*? '"' ; // matches escape characters
CHAR_LIT: '\'' .*? '\'';

RSTR_LIT: ('r'|'R') STR_LIT; // doesnt match escape characters
GENERALIZED_STR_LIT: IDENTIFIER'('RSTR_LIT')' | IDENTIFIER STR_LIT;
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER'('TRIPLESTR_LIT')' | IDENTIFIER TRIPLESTR_LIT;

IDENTIFIER : LETTER+ ('_'? (LETTER | DIGIT))*;
DIGIT : [0-9] ;
LETTER : [a-zA-Z] ;

INT_LIT : HEX_LIT
        | DEC_LIT
        | OCT_LIT
        | BIN_LIT ;

// NUMERALS
HEXDIGIT : DIGIT | [A-F] | [a-f] ;
OCTDIGIT : [0-7] ;
BINDIGIT : [0-1] ;

HEX_LIT : '0' ('x' | 'X' ) HEXDIGIT ('_'? HEXDIGIT)* ;
DEC_LIT : DIGIT+ ('_'? DIGIT)* ;
OCT_LIT : '0' ('o' | 'O') OCTDIGIT ('_'? OCTDIGIT)* ;
BIN_LIT : '0' ('b' | 'B' ) BINDIGIT ('_'? BINDIGIT)* ;

INT8_LIT : INT_LIT '\'' ('i' | 'I') '8' ;
INT16_LIT : INT_LIT '\'' ('i' | 'I') '16' ;
INT32_LIT : INT_LIT '\'' ('i' | 'I') '32' ;
INT64_LIT : INT_LIT '\'' ('i' | 'I') '64' ;

UINT_LIT : INT_LIT '\'' ('u' | 'U') ;
UINT8_LIT : INT_LIT '\'' ('u' | 'U') '8' ;
UINT16_LIT : INT_LIT '\'' ('u' | 'U') '16' ;
UINT32_LIT : INT_LIT '\'' ('u' | 'U') '32' ;
UINT64_LIT : INT_LIT '\'' ('u' | 'U') '64' ;

EXP : ('e' | 'E' ) ('+' | '-') DIGIT ('_'? DIGIT)* ;
FLOAT_LIT : DIGIT ('_'? DIGIT)* (('.' DIGIT ('_'? DIGIT)* EXP?) |EXP) ;
FLOAT32_SUFFIX : ('f' | 'F') '32'? ;
FLOAT32_LIT : HEX_LIT '\'' FLOAT32_SUFFIX
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT32_SUFFIX;
FLOAT64_SUFFIX : (('f' | 'F') '64') | 'd' | 'D';
FLOAT64_LIT : HEX_LIT '\'' FLOAT64_SUFFIX
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT64_SUFFIX;
