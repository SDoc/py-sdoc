"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc


class Format(metaclass=abc.ABCMeta):
    """
    Abstract parent class for all formatters for generating output documents in a certain format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, config):
        """
        Object constructor.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        :param configparser.ConfigParser config: The section in the config file for the target_format.
        """
        self._io = io
        """
        The IO object.

        :type: cleo.styles.output_style.OutputStyle
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
    @abc.abstractmethod
    def generate(self):
        """
        Generating the document in the target format and returns the number of error encountered.

        :rtype: int
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
