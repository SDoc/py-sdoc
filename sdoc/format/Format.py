import abc

from cleo.io.io import IO


class Format(metaclass=abc.ABCMeta):
    """
    Abstract parent class for all formatters for generating output documents in a certain format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        """
        self._io: IO = io
        """
        The IO object.
        """

        self._errors: int = 0
        """
        The error count.
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def errors(self) -> int:
        """
        Getter for the error count.
        """
        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def generate(self) -> int:
        """
        Generating the document in the target format and returns the number of error encountered.
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
