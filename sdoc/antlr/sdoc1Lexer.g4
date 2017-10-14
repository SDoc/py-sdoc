lexer grammar sdoc1Lexer;

// Default mode TEXT.
TEXT
  : ~[\\]+
  | '\\\\';

LINE_COMMENT
  : COMMENT ~[\r\n]* [\r\n]
  ;

// SDoc1 keywords
COMMENT:    '\\comment';
DEBUG:      '\\debug'           -> mode(MODE_EXPR);
ELIF:       '\\elif'            -> mode(MODE_EXPR);
ELSE:       '\\else';
ENDIF:      '\\endif';
ERROR:      '\\error'           -> mode(MODE_SIMPLE);
EXPRESSION: '\\expression'      -> mode(MODE_EXPR);
IF:         '\\if'              -> mode(MODE_EXPR);
INCLUDE:    '\\include'         -> mode(MODE_SIMPLE);
NOTICE:     '\\notice'          -> mode(MODE_SIMPLE);
SUBSTITUTE: '\\substitute'      -> mode(MODE_EXPR);

// All other tokens starting with \ are considered SDoc2 commands.
SDOC2_COMMAND: '\\'[a-z_]+;


// Mode for SDoc1 commands with a simple argument, i.e. \notice{Hello World}
mode MODE_SIMPLE;

SIMPLE_OBRACE:  '{';
SIMPLE_CBRACE:  '}'  -> mode(DEFAULT_MODE);
SIMPLE_ARG:     (~[{}] | '\\'. )+;


// Mode for SDoc1 commands with an expression as argument, i.e. \expression{a=b=c='abc'}
mode MODE_EXPR;

EXPR_OBRACE: '{';
EXPR_CBRACE: '}'  -> mode(DEFAULT_MODE);
EXPR_WS:     [ \r\t\n]+ -> channel(HIDDEN);

EXPR_LEFT_PAREN :   '(';
EXPR_RIGHT_PAREN :  ')';
EXPR_LEFT_BRACKET:  '[';
EXPR_RIGHT_BRACKET: ']';

EXPR_MULT:  '*';
EXPR_DIV:   '/';
EXPR_ADD:   '+';
EXPR_MINUS: '-';

EXPR_EQUAL:       '==';
EXPR_GT:          '>';
EXPR_GTE:         '>=';
EXPR_LOGICAL_AND: '&&';
EXPR_LOGICAL_OR:  '||';
EXPR_LT:          '<';
EXPR_LTE:         '<=';
EXPR_NOT_EQUAL:   '!=';

EXPR_ASSIGN:      '=';

EXPR_IDENTIFIER
    :   EXPR_NON_DIGIT
        (   EXPR_NON_DIGIT
        |   EXPR_DIGIT
        )*
    ;

EXPR_INTEGER_CONSTANT
    :   EXPR_DIGIT+
    ;

fragment
EXPR_NON_DIGIT
    :   [a-zA-Z_]
    ;

fragment
EXPR_DIGIT
    :   [0-9]
    ;

fragment
ESCAPED_CHAR : '\\\\' | '\\\'';

EXPR_STRING_CONSTANT
    :   '\'' ( ESCAPED_CHAR | ~['])*? '\''
    ;
