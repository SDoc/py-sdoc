"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""


# ----------------------------------------------------------------------------------------------------------------------
class SDocVisitor:
    """
    Parent visitor for SDoc level 1 & 2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io):
        """
        Object constructor.
        """

        self._io = io
        """
        Styled output formatter.

        :type: sdoc.style.SdocStyle.SdocStyle
        """

        self._errors = 0
        """
        The error count.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def errors(self):
        """
        Getter for the error count.

        :rtype: int
        """
        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def _error(self, message, token=None):
        """
        Logs an error.

        :param str message: The error message.This message will be appended with 'at filename:line.column' ot the token.
        :param antlr4.Token.CommonToken token: The token where the error occurred.
        """
        self._errors += 1

        filename = token.getInputStream().fileName  # Replace fileName with get_source_name() when implemented in ANTLR.
        line_number = token.line
        column_number = token.column + 1
        messages = [message]
        if token:
            messages.append('Position: {0!s}:{1:d}.{2:d}'.format(filename, line_number, column_number))
        self._io.error(messages)


# ----------------------------------------------------------------------------------------------------------------------
