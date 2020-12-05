import abc
from configparser import ConfigParser

from cleo.styles import OutputStyle


class Format(metaclass=abc.ABCMeta):
    """
    Abstract parent class for all formatters for generating output documents in a certain format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: OutputStyle, config: ConfigParser):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param ConfigParser config: The section in the config file for the target_format.
        """
        self._io: OutputStyle = io
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
