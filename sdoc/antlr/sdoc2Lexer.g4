lexer grammar sdoc2Lexer;

// Default mode TEXT.
TEXT
  : ~[\\]+
  | '\\\\';

// SDoc2 keywords
BEGIN:      '\\begin'    -> pushMode(MODE_BLOCK_ARG);
END:        '\\end'      -> pushMode(MODE_BLOCK_ARG);

POSITION:   '\\position' -> pushMode(MODE_INLINE_ARG);

// All other tokens starting with \ are considered SDoc2 line commands.
SDOC2_COMMAND: '\\'[a-z_][a-z0-9_]*  -> pushMode(MODE_INLINE_ARG);


mode MODE_BLOCK_ARG;

BLOCK_ARG_LEFT_BRACKET: '['  -> pushMode(MODE_OPT_ARG);
BLOCK_ARG_LEFT_BRACE:   '{'  -> pushMode(BLOCK_MODE_ARG);

BLOCK_ARG_WS: [ \t\r\n]+ -> skip;

// Mode for main argument.
mode BLOCK_MODE_ARG;

BLOCK_ARG_RIGHT_BRACE:  '}'[ \t\r\n]*  -> popMode,popMode;

BLOCK_ARG_ARG: (~[{}] | '\\'. )+;

// Mode for SDoc2 commands with an argument, i.e. \chapter[]{What is SDoc?}
mode MODE_INLINE_ARG;

INLINE_ARG_LEFT_BRACKET: '['  -> pushMode(MODE_OPT_ARG);
INLINE_ARG_LEFT_BRACE:   '{'  -> pushMode(INLINE_MODE_ARG);


// Mode for optinal arguments.
mode MODE_OPT_ARG;

OPT_ARG_RIGHT_BRACKET: ']'  -> popMode;
OPT_ARG_EQUALS:        '=';

OPT_ARG_NAME: [a-zA-Z][a-zA-Z0-9_]*;

OPT_ARG_VALUE
   : OPT_ARG_STRING
   | OPT_ARG_INT
   ;

fragment
OPT_ARG_STRING
   :   '"' ~["]* '"'
   |   '\'' ~[']* '\''
   ;

fragment
OPT_ARG_INT: [0-9]+;

OPT_ARG_WS: [ \t\r\n]+ -> skip ;


// Mode for main argument.
mode INLINE_MODE_ARG;

INLINE_ARG_RIGHT_BRACE:  '}'  -> popMode,popMode;

INLINE_ARG_ARG: (~[{}] | '\\'. )+;


