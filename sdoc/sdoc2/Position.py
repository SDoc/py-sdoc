"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
import os


class Position:
    """
    Class for start and end position of a node in a SDoc source file.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, file_name, start_line, start_column, end_line, end_column):
        """
        Object constructor.

        :param str file_name: The name of the file where the node is defined.
        :param int start_line: The line where the node definition starts.
        :param int start_column: The column where the node definition starts.
        :param int end_line: The line where the node definition ends.
        :param int end_column: The column where the node definition end.
        """
        self.file_name = file_name
        """
        The name of the file where the node is defined.

        :type: str
        """

        self.start_line = start_line
        """
        The line where the node definition starts.

        :type: int
        """

        self.start_column = start_column
        """
        The column where the node definition starts.

        :type: int
        """

        self.end_line = end_line
        """
        The line where the node definition ends.

        :type: int
        """
        self.end_column = end_column
        """
        The column where the node definition end.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """
        String representation of the position.

        :rtype: str
        """
        if not self.file_name:
            return "{0:d}.{1:d}".format(self.start_line, self.start_column + 1)

        return "{0!s}:{1:d}.{2:d}".format(os.path.relpath(self.file_name), self.start_line, self.start_column+1)


# ----------------------------------------------------------------------------------------------------------------------
