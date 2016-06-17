"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc


class Format:
    """
    Abstract parent class for all formatters for generating output documents in a certain format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, config):
        """
        Object constructor.

        :param configparser.SectionProxy config: The section in the config file for the target_format.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def generate(self):
        """
        Starts generating HTML file.
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
