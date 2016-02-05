parser grammar sdoc2Parser;

options { tokenVocab=sdoc2Lexer; }

sdoc: (command|text)*;

text: TEXT;

// All SDoc2 commands.
command
  : cmd_begin
  | cmd_end
  | cmd_position

  | cmd_sdoc2   // Note: This command MUST be the last alternative of all commands.
  ;

// Begin command. Start a block command, e.g. \begin{itemize}
cmd_begin:
   BEGIN
   (BLOCK_ARG_LEFT_BRACKET (OPT_ARG_NAME OPT_ARG_EQUALS OPT_ARG_VALUE)* OPT_ARG_RIGHT_BRACKET)?
   BLOCK_ARG_LEFT_BRACE BLOCK_ARG_ARG BLOCK_ARG_RIGHT_BRACE;

// End command. The end of a block command, e.g. \end{itemize}
cmd_end: END BLOCK_ARG_LEFT_BRACE BLOCK_ARG_ARG BLOCK_ARG_RIGHT_BRACE;

// SDoc2 command position
cmd_position:
    POSITION
    (INLINE_ARG_LEFT_BRACKET (OPT_ARG_NAME OPT_ARG_EQUALS OPT_ARG_VALUE)* OPT_ARG_RIGHT_BRACKET)?
    (INLINE_ARG_LEFT_BRACE INLINE_ARG_ARG? INLINE_ARG_RIGHT_BRACE)?;

// Other SDoc2 commands.
cmd_sdoc2:
    SDOC2_COMMAND
    (INLINE_ARG_LEFT_BRACKET (OPT_ARG_NAME OPT_ARG_EQUALS OPT_ARG_VALUE)* OPT_ARG_RIGHT_BRACKET)?
    (INLINE_ARG_LEFT_BRACE INLINE_ARG_ARG? INLINE_ARG_RIGHT_BRACE)?;

