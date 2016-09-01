parser grammar sdoc1Parser;

options { tokenVocab=sdoc1Lexer; }

sdoc: (command|text)*;

text: TEXT;

// All SDoc1 commands.
command
  : cmd_comment
  | cmd_debug
  | cmd_expression
  | cmd_error
  | cmd_if
  | cmd_include
  | cmd_notice
  | cmd_substitute

  | cmd_sdoc2   // Note: This command MUST be the last alternative of all commands.
  ;


// Comment command. Does nothing.
cmd_comment: LINE_COMMENT;

// Bebug command. Prints the value of an expression.
cmd_debug: DEBUG EXPR_OBRACE expression? EXPR_CBRACE;

// Expression command. Sets one or more variables.
cmd_expression: EXPRESSION EXPR_OBRACE expression EXPR_CBRACE;

// Error command. Logs an error messages and increases the error count.
cmd_error: ERROR SIMPLE_OBRACE SIMPLE_ARG SIMPLE_CBRACE;

// If-then-else command.
cmd_if: IF EXPR_OBRACE expression EXPR_CBRACE sdoc
        (ELIF EXPR_OBRACE expression EXPR_CBRACE sdoc)*
        (ELSE sdoc)?
        ENDIF;

// Include command. Includes a SDoc resource.
cmd_include: INCLUDE SIMPLE_OBRACE SIMPLE_ARG SIMPLE_CBRACE;

// Notice command. Prints message on console.
cmd_notice: NOTICE SIMPLE_OBRACE SIMPLE_ARG SIMPLE_CBRACE;

// Substitute command. Substitues the value of an expression in to SDoc2 output.
cmd_substitute: SUBSTITUTE EXPR_OBRACE expression EXPR_CBRACE;

// SDoc2 command. Passed through to the output without modifications.
cmd_sdoc2: SDOC2_COMMAND;

// Expression stuff.
primaryExpression
    :   EXPR_IDENTIFIER                              # primaryExpressionIdentifier
    |   EXPR_INTEGER_CONSTANT                        # primaryExpressionIntegerConstant
    |   EXPR_STRING_CONSTANT                         # primaryExpressionStringConstant
    |   EXPR_LEFT_PAREN expression EXPR_RIGHT_PAREN  # primaryExpressionSubExpression
    ;

postfixExpression
    :   primaryExpression                                                  # primaryExpressionParent
    |   postfixExpression EXPR_LEFT_BRACKET expression EXPR_RIGHT_BRACKET  # postfixExpressionExpression
    ;

multiplicativeExpression
    :   postfixExpression
    |   multiplicativeExpression EXPR_MULT postfixExpression
    |   multiplicativeExpression EXPR_DIV postfixExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression EXPR_ADD multiplicativeExpression
    |   additiveExpression EXPR_MINUS multiplicativeExpression
    ;

relationalExpression
    :   additiveExpression
    |   relationalExpression EXPR_LT additiveExpression
    |   relationalExpression EXPR_GT additiveExpression
    |   relationalExpression EXPR_LTE additiveExpression
    |   relationalExpression EXPR_GTE additiveExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression EXPR_EQUAL relationalExpression
    |   equalityExpression EXPR_NOT_EQUAL relationalExpression
    ;

logicalAndExpression
    :   equalityExpression                                       # logicalAndExpressionParent
    |   logicalAndExpression EXPR_LOGICAL_AND equalityExpression # logicalAndExpressionAnd
    ;

logicalOrExpression
    :   logicalAndExpression                                     # logicalOrExpressionParent
    |   logicalOrExpression EXPR_LOGICAL_OR logicalAndExpression # logicalOrExpressionLogicalOr
    ;

assignmentExpression
    :   logicalOrExpression                                       # assignmentExpressionParent
    |   postfixExpression assignmentOperator assignmentExpression # assignmentExpressionAssignment
    ;

assignmentOperator
    :   EXPR_ASSIGN
    ;

expression
    :   assignmentExpression
    ;
