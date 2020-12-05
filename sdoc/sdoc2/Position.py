import os


class Position:
    """
    Class for start and end position of a node in a SDoc source file.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, file_name: str, start_line: int, start_column: int, end_line: int, end_column: int):
        """
        Object constructor.

        :param str file_name: The name of the file where the node is defined.
        :param int start_line: The line where the node definition starts.
        :param int start_column: The column where the node definition starts.
        :param int end_line: The line where the node definition ends.
        :param int end_column: The column where the node definition end.
        """
        self.file_name: str = file_name
        """
        The name of the file where the node is defined.
        """

        self.start_line: int = start_line
        """
        The line where the node definition starts.
        """

        self.start_column: int = start_column
        """
        The column where the node definition starts.
        """

        self.end_line: int = end_line
        """
        The line where the node definition ends.
        """
        self.end_column: int = end_column
        """
        The column where the node definition end.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        """
        String representation of the position.
        """
        if not self.file_name:
            return "{0:d}.{1:d}".format(self.start_line, self.start_column + 1)

        return "{0!s}:{1:d}.{2:d}".format(os.path.relpath(self.file_name), self.start_line, self.start_column + 1)

# ----------------------------------------------------------------------------------------------------------------------
