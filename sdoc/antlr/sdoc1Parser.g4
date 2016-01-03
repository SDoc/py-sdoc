parser grammar sdoc1Parser;

options { tokenVocab=sdoc1Lexer; }

sdoc: (command|text)*;

text: TEXT;

// All SDoc1 commands
command
  : cmd_comment
  | cmd_debug
  | cmd_expression
  | cmd_if
  | cmd_notice
  | cmd_sdoc2
  ;

// Expression command.
cmd_expression: EXPRESSION EXPR_OBRACE expression EXPR_CBRACE;

// If-then-else command.
cmd_if: IF EXPR_OBRACE expression EXPR_CBRACE sdoc
        (ELIF EXPR_OBRACE expression EXPR_CBRACE sdoc)*
        (ELSE sdoc)?
        ENDIF;

// Comment command.
cmd_comment: LINE_COMMENT;

// Bebug command. Prints the value of an expression.
cmd_debug: DEBUG EXPR_OBRACE expression? EXPR_CBRACE;

// Notice command. Prints message on colsole.
cmd_notice: NOTICE NOTICE_OBRACE NOTICE_MESSAGE NOTICE_CBRACE;

//
cmd_sdoc2: SDOC2_COMMAND;

primaryExpression
    :   IDENTIFIER        # primaryExpressionIdentifier
    |   INTEGER_CONSTANT  # primaryExpressionIntegerConstant
    |   STRING_CONSTANT   # primaryExpressionStringConstant
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression OBRACKET expression CBRACKET
    ;

multiplicativeExpression
    :   postfixExpression
    |   multiplicativeExpression MULT postfixExpression
    |   multiplicativeExpression DIV postfixExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression ADD multiplicativeExpression
    |   additiveExpression MINUS multiplicativeExpression
    ;

relationalExpression
    :   additiveExpression
    |   relationalExpression LT additiveExpression
    |   relationalExpression GT additiveExpression
    |   relationalExpression LTE additiveExpression
    |   relationalExpression GTE additiveExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression EQUAL relationalExpression
    |   equalityExpression NOT_EQUAL relationalExpression
    ;

logicalAndExpression
    :   equalityExpression
    |   logicalAndExpression LOGICAL_AND equalityExpression
    ;

logicalOrExpression
    :   logicalAndExpression                                # logicalOrExpressionParent
    |   logicalOrExpression LOGICAL_OR logicalAndExpression # logicalOrExpressionLogicalOr
    ;

assignmentExpression
    :   logicalOrExpression                                       # assignmentExpressionParent
    |   postfixExpression assignmentOperator assignmentExpression # assignmentExpressionAssignment
    ;

assignmentOperator
    :   ASSIGN
    ;

expression
    :   assignmentExpression
    ;
