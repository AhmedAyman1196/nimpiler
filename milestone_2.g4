grammar milestone_2;

// ------------------------------ Grammar --------------------------------------

tokens { INDENT, DEDENT }

@lexer::members {

import queue

# A queue where extra tokens are pushed on (see the NEWLINE lexer rule).
tokens = queue.Queue()
# The stack that keeps track of the indentation level.
indents = []
# The amount of opened braces, brackets and parenthesis.
opened = 0
# The most recently produced token.
lastToken = None

def emit(self, t):
    super.setToken(t)
    tokens.offer(t)

def nextToken(self):
    # Check if the end-of-file is ahead and there are still some DEDENTS expected.
    if self._input.LA(1) == Token.EOF and this.indents:
        # Remove any trailing EOF tokens from our buffer.
        for j in range(0, len(tokens)):
            i = len(tokens) - 1 - j
            if tokens.get(i).getType() == EOF:
                tokens.remove(i)

    # Now emit as much DEDENT tokens as needed.
    while indents:
        this.emit(createDedent())
        indents.pop()

    # Put the EOF back on the token stream.
    this.emit(commonToken(Token.EOF, "<EOF>"))

    next = super.nextToken()

    if next.getChannel() == Token.DEFAULT_CHANNEL:
        # Keep track of the last token on the default channel.
        this.lastToken = next

    return next if not tokens else tokens.poll()

def createDedent(self):
    dedent = commonToken(milestone_2Parser.DEDENT, "")
    dedent.setLine(this.lastToken.getLine())
    return dedent

def commonToken(self, type, text):
    stop = this.getCharIndex() - 1
    start = stop if not text else stop - len(text) + 1
    return CommonToken(this._tokenFactorySourcePair, type, DEFAULT_TOKEN_CHANNEL, start, stop)

# Calculates the indentation of the provided spaces, taking the
# following rules into account:
#
# "Tabs are replaced (from left to right) by one to four spaces
#  such that the total number of characters up to and including
#  the replacement is a multiple of four [...]"
@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces.toCharArray():
        if ch == '\t':
            count += 4 - (count % 4)
            break
        else:
            # A normal space char.
            count += 1
    return count

def atStartOfInput(self):
    return super.getCharPositionInLine() == 0 and super.getLine() == 1
}

module : (stmt ((';' | 'IND{=}') stmt)*)? ;

comma : ',' COMMENT? ;
semicolon : ';' COMMENT? ;
colon : ':' COMMENT? ;
colcom : ':' COMMENT? ;
operator :  OP0 | OP1 | OP2 | OP3 | OP4 | OP5 | OP6 | OP7 | OP8 | OP9
         | 'or' | 'xor' | 'and'
         | 'is' | 'isnot' | 'in' | 'notin' | 'of'
         | 'div' | 'mod' | 'shl' | 'shr' | 'not' | 'static' | '..' ;

OP10 : '^';
OP9 : MUL_OPERATOR | DIV_OPERATOR | DIV | SHL | SHR | MODULUS;
OP8 : ADD_OPERATOR | MINUS_OPERATOR;
OP7 : AND_OPERATOR;
OP6 : '..';
OP5 : '==' | '<=' | '<' | '>=' | '>' | '!=' | IN | NOTIN | IS | ISNOT | NOT | OF;
OP4 : AND;
OP3 : OR | XOR;
OP2 : AT | COLON | '?';
OP1 : '=' | '+=' | '-=' | '*=' | '/=';
OP0 : '->' | '~>' | '=>';
opr : OP9 | OP8;

prefixOperator : operator ;
optInd : COMMENT? 'IND'? ;
optPar : ('IND{>}' | 'IND{=}')? ;

simpleExpr : arrowExpr (OP0 optInd arrowExpr)* pragma? ;
arrowExpr : assignExpr (OP1 optInd assignExpr)* ;
assignExpr : orExpr (OP2 optInd orExpr)* ;
orExpr : andExpr (OP3 optInd andExpr)*;
andExpr : cmpExpr (OP4 optInd cmpExpr)* ;
cmpExpr : sliceExpr (OP5 optInd sliceExpr)*;
sliceExpr : ampExpr (OP6 optInd ampExpr)* ;
ampExpr : plusExpr (OP7 optInd plusExpr)* ;
plusExpr : mulExpr (OP8 optInd mulExpr)* ;
mulExpr : dollarExpr (OP9 optInd dollarExpr)* ;
dollarExpr : primary (OP10 optInd primary)* ;
symbol : ('`' (KEYW|ident|literal|(operator|'('|')'|'['|']'|'{'|'}'|'=')+)+ '`') | ident | KEYW ;

exprColonEqExpr : expr (':'|'=' expr)?;

exprList : expr (comma expr)* ;

exprColonEqExprList : exprColonEqExpr (comma exprColonEqExpr)* (comma)? ;
dotExpr : expr '.' optInd (symbol | '[:' exprList ']') ;
explicitGenericInstantiation : '[:' exprList ']' ( '(' exprColonEqExpr ')' )? ;
qualifiedIdent : symbol ('.' optInd symbol)? ;
setOrTableConstr : '{' ((exprColonEqExpr comma)* | ':' ) '}' ;
castExpr : 'cast' '[' optInd typeDesc optPar ']' '(' optInd expr optPar ')' ;
parKeyw : 'discard' | 'include' | 'if' | 'while' | 'case' | 'try'
        | 'finally' | 'except' | 'for' | 'block' | 'const' | 'let'
        | 'when' | 'var' | 'mixin' ;


par : '(' optInd
          ( complexOrSimpleStmt (';' complexOrSimpleStmt)*
          | ';' complexOrSimpleStmt (';' complexOrSimpleStmt)*
          | pragmaStmt
          | simpleExpr ( ('=' expr (';' complexOrSimpleStmt (';' complexOrSimpleStmt)* )? )
                       | (':' expr (',' exprColonEqExpr (',' exprColonEqExpr)* )? ) ) )
          optPar ')' ;

literal : INT_LIT | INT8_LIT | INT16_LIT | INT32_LIT | INT64_LIT
          | UINT_LIT | UINT8_LIT | UINT16_LIT | UINT32_LIT | UINT64_LIT
          | FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT
          | STR_LIT | RSTR_LIT | TRIPLESTR_LIT
          | CHAR_LIT
          | NIL ;
generalizedLit : GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT ;
identOrLiteral : generalizedLit | symbol | literal
               | par | arrayConstr | setOrTableConstr
               | castExpr ;
tupleConstr : '(' optInd (exprColonEqExpr comma?)* optPar ')' ;
arrayConstr : '[' optInd (exprColonEqExpr comma?)* optPar ']' ;

primarySuffix : '(' (exprColonEqExpr comma?)* ')' doBlocks?
      | doBlocks
      | '.' optInd symbol generalizedLit?
      | '[' optInd indexExprList optPar ']'
      | '{' optInd indexExprList optPar '}'
      | expr;

indexExprList : indexExpr (comma indexExpr)*;
indexExpr : expr;

macroColon : ':' stmt? ( 'IND{=}' 'of' exprList ':' stmt
                       | 'IND{=}' 'elif' expr ':' stmt
                       | 'IND{=}' 'except' exprList ':' stmt
                       | 'IND{=}' 'else' ':' stmt )*;

moduleName : IDENTIFIER ('.'IDENTIFIER)*?;

exportStmt : 'import' optInd expr
              ((comma expr)*
              | 'except' optInd (expr (comma expr)*)) ;

ident : IDENTIFIER;

doBlocks : (doBlock ('IND{=}' doBlock)*);

caseExpr : caseStmt;

condExpr : expr colcom expr optInd
        ('elif' expr colcom expr optInd)*
         'else' colcom expr ;
ifExpr : 'if' condExpr ;
whenExpr : 'when' condExpr ;
pragma : '{.' optInd (exprColonEqExpr comma?)* optPar ('.}' | '}') ;

identVis : symbol opr?;

identVisDot : symbol '.' optInd symbol opr? ;
identWithPragma : identVis pragma? ;
identWithPragmaDot : identVisDot pragma? ;
declColonEquals : identWithPragma (comma identWithPragma)* comma?
                  (':' optInd typeDesc)? ('=' optInd expr)? ;
identColonEquals : ident (comma ident)* comma?
     (':' optInd typeDesc)? ('=' optInd expr)? ;

inlTupleDecl : 'tuple'
    '[' optInd  (identColonEquals (comma/semicolon)?)*  optPar ']' ;

extTupleDecl : 'tuple'
    COMMENT? ('IND{>}' identColonEquals ('IND{=}' identColonEquals)*)? ;
tupleClass : 'tuple' ;

paramList : '(' (declColonEquals ((comma'/'semicolon) declColonEquals)*)? ')' ;

paramListArrow : paramList? ('->' optInd typeDesc)? ;
paramListColon : paramList? (':' optInd typeDesc)? ;
doBlock : 'do' paramListArrow pragma? colcom stmt ;
procExpr : 'proc' paramListColon pragma? ('=' COMMENT? stmt)? ;
distinct : 'distinct' optInd typeDesc ;

forStmt : 'for' (identWithPragma (comma identWithPragma)*) 'in' expr colcom stmt ;
forExpr : forStmt ;


expr : (blockExpr
      | ifExpr
      | whenExpr
      | caseExpr
      | forExpr
      | tryExpr)
      | simpleExpr ;
typeKeyw : 'var' | 'out' | 'ref' | 'ptr' | 'shared' | 'tuple'
         | 'proc' | 'iterator' | 'distinct' | 'object' | 'enum' ;

primary : typeKeyw typeDesc
        | prefixOperator* identOrLiteral primarySuffix*
        | 'bind' primary ;


typeDesc : simpleExpr ;
typeDefAux : simpleExpr
           | 'concept' typeClass ;
postExprBlocks : ':' stmt? ( 'IND{=}' doBlock
                           | 'IND{=}' 'of' exprList ':' stmt
                           | 'IND{=}' 'elif' expr ':' stmt
                           | 'IND{=}' 'except' exprList ':' stmt
                           | 'IND{=}' 'else' ':' stmt )* ;


exprStmt : simpleExpr
         (( '=' optInd expr colonBody? )
         | ( expr (comma expr)*
             doBlocks
              | macroColon
           ))? ;

importStmt : 'import' optInd expr
              ((comma expr)*
              | 'except' optInd (expr (comma expr)*)) ;

includeStmt : 'include' optInd expr (comma expr)* ;

fromStmt : 'from' moduleName 'import' optInd expr (comma expr)* ;
returnStmt : 'return' optInd expr? ;
raiseStmt : 'raise' optInd expr? ;
yieldStmt : 'yield' optInd expr? ;
discardStmt : 'discard' optInd expr? ;
breakStmt : 'break' optInd expr? ;
continueStmt : 'break' optInd expr? ;
condStmt : expr colcom stmt COMMENT?
           ('IND{=}' 'elif' expr colcom stmt)*
           ('IND{=}' 'else' colcom stmt)? ;
ifStmt : 'if' condStmt  ;
whenStmt : 'when' condStmt ;
whileStmt : 'while' expr colcom stmt ;
ofBranch : 'of' exprList colcom stmt ;
ofBranches : ofBranch ('IND{=}' ofBranch)*
                      ('IND{=}' 'elif' expr colcom stmt)*
                      ('IND{=}' 'else' colcom stmt)? ;
caseStmt : 'case' expr ':'? COMMENT?
            ('IND{>}' ofBranches 'DED'
            | 'IND{=}' ofBranches) ;

tryStmt : 'try' colcom stmt
           ('IND{=}'? 'except' exprList colcom stmt)*
           ('IND{=}'? 'finally' colcom stmt)? ;

tryExpr : 'try' colcom stmt
           (optInd 'except' exprList colcom stmt)*
           (optInd 'finally' colcom stmt)? ;

exceptBlock : 'except' colcom stmt ;
blockStmt : 'block' symbol? colcom stmt ;
blockExpr : 'block' symbol? colcom stmt ;
staticStmt : 'static' colcom stmt ;
deferStmt : 'defer' colcom stmt ;
asmStmt : 'asm' pragma? (STR_LIT | RSTR_LIT | TRIPLESTR_LIT) ;
genericParam : symbol (comma symbol)* (colon expr)? ('=' optInd expr)? ;

genericParamList : '[' optInd
  (genericParam ((comma|semicolon) genericParam)*)? optPar ']' ;

pattern : '{' stmt '}' ;
indAndComment : ('IND{>}' COMMENT)? | COMMENT? ;
routine : optInd identVis pattern? genericParamList?
  paramListColon pragma? ('=' COMMENT? stmt)? indAndComment ;
commentStmt : COMMENT ;

sectionTypeDef : COMMENT? typeDef | ('IND{>}' (typeDef | COMMENT) ('IND{=}' (typeDef | COMMENT))* 'DED') ;
sectionConstant : COMMENT? constant | ('IND{>}' (constant | COMMENT) ('IND{=}' (constant | COMMENT))* 'DED') ;
sectionVariable : COMMENT? variable | ('IND{>}' (variable | COMMENT) ('IND{=}' (variable | COMMENT))* 'DED') ;

constant : identWithPragma (colon typeDesc)? '=' optInd expr indAndComment ;
enum : 'enum' optInd (symbol optInd ('=' optInd expr COMMENT?)? comma?)+ ;
objectWhen : 'when' expr colcom objectPart COMMENT?
            ('elif' expr colcom objectPart COMMENT?)*
            ('else' colcom objectPart COMMENT?)? ;
objectBranch : 'of' exprList colcom objectPart ;
objectBranches : objectBranch ('IND{=}' objectBranch)*
                      ('IND{=}' 'elif' expr colcom objectPart)*
                      ('IND{=}' 'else' colcom objectPart)? ;
objectCase : 'case' identWithPragma ':' typeDesc ':'? COMMENT?
            ('IND{>}' objectBranches 'DED'
            | 'IND{=}' objectBranches) ;

objectPart : 'IND{>}' objectPart ('IND{=}' objectPart)* 'DED'
           | objectWhen | objectCase | 'nil' | 'discard' | declColonEquals ;

// renamed from object
objectX : 'object' pragma? ('of' typeDesc)? COMMENT? objectPart ;
typeClassParam : ('var' | 'out')? symbol ;

typeClass : (typeClassParam (',' typeClassParam)*)? (pragma)? ('of' (typeDesc (',' typeDesc)*)?)?
              | stmt ;

typeDef : identWithPragmaDot genericParamList? '=' optInd typeDefAux
            indAndComment? ;

varTuple : '(' optInd identWithPragma (comma identWithPragma)* optPar ')' '=' optInd expr ;

colonBody : colcom stmt doBlocks? ;

variable : (varTuple | identColonEquals) colonBody? indAndComment ;

bindStmt : 'bind' optInd qualifiedIdent (comma qualifiedIdent)* ;

mixinStmt : 'mixin' optInd qualifiedIdent (comma qualifiedIdent)* ;

pragmaStmt : pragma (':' COMMENT? stmt)? ;

simpleStmt : ((returnStmt | raiseStmt | yieldStmt | discardStmt | breakStmt
           | continueStmt | pragmaStmt | importStmt | exportStmt | fromStmt
           | includeStmt | commentStmt) | exprStmt) COMMENT? ;

complexOrSimpleStmt : (ifStmt | whenStmt | whileStmt
                    | tryStmt | forStmt
                    | blockStmt | staticStmt | deferStmt | asmStmt
                    | 'proc' routine
                    | 'method' routine
                    | 'iterator' routine
                    | 'macro' routine
                    | 'template' routine
                    | 'converter' routine
                    | 'type' sectionTypeDef
                    | 'const' sectionConstant
                    | ('let' | 'var' | 'using') sectionVariable
                    | bindStmt | mixinStmt)
                    | simpleStmt ;


stmt : ('IND{>}' complexOrSimpleStmt (('IND{=}' | ';') complexOrSimpleStmt)* 'DED')
     | simpleStmt (';' simpleStmt)* ;


// =============================================================================
// ============================ Lexical Analysis ===============================

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
KEYW :
AND | VARIABLE|ADDR |AS | ASM |BIND |BLOCK |BREAK |CASE |CAST |CONCEPT |CONST |CONTINUE | CONVERTER |DEFER |
DISCARD |DISTINCT |DIV |DO |ELIF |ELSE |END |ENUM |EXCEPT |EXPORT |FINALLY | FOR |FROM |FUNC |IF |IMPORT |
IN |INCLUDE| INTERFACE |IS |ISNOT | ITERATOR |LET | MACRO |METHOD |MIXIN |MOD |NIL |NOT |NOTIN |OBJECT |
OF |OR |OUT  |PROC |PTR |RAISE |REF |RETURN |SHL |SHR |STATIC | TEMPLATE | TRY |TUPLE |TYPE |USING |WHEN |
WHILE |XOR |YIELD ;

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

start : module;
