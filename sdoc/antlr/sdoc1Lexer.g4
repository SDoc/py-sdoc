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
EXPRESSION: '\\expression'      -> mode(MODE_EXPR);
IF:         '\\if'              -> mode(MODE_EXPR);
NOTICE:     '\\notice'          -> mode(MODE_NOTICE);

// All other tokens starting with \ are considered SDoc2 commands.
SDOC2_COMMAND: '\\'[a-z_]+;


mode MODE_NOTICE;

NOTICE_OBRACE:  '{';
NOTICE_CBRACE:  '}'  -> mode(DEFAULT_MODE);
NOTICE_MESSAGE: (~[\{\}] | '\\'. )+;


mode MODE_EXPR;

EXPR_OBRACE: '{';
EXPR_CBRACE: '}'  -> mode(DEFAULT_MODE);
EXPR_WS:     [ \r\t\n]+ -> channel(HIDDEN);

OBRACKET:    '[';
CBRACKET:    ']';

MULT:        '*';
DIV:         '/';
ADD:         '+';
MINUS:       '-';

EQUAL:       '==';
GT:          '>';
GTE:         '>=';
LOGICAL_AND: '&&';
LOGICAL_OR:  '||';
LT:          '<';
LTE:         '<=';
NOT_EQUAL:   '!=';

ASSIGN:      '=';

IDENTIFIER
    :   Nondigit
        (   Nondigit
        |   Digit
        )*
    ;

INTEGER_CONSTANT
    :   Digit+
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

STRING_CONSTANT
    :   '\'' ~['\\\r\n]* '\''
    ;