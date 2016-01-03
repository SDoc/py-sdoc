"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc


class DataType:
    """
    Abstract parent class for all data types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def debug(self):
        """
        Returns a string for debugging.

        :rtype: str
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def get_value(self):
        """
        Returns the underling value of this data type.

        :rtype: str|int
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_constant(self):
        """
        Returns True if this data type is a constant. Returns False otherwise.

        :rtype: bool
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_scalar(self):
        """
        Returns True if this data type is a scalar. Returns False otherwise.

        :rtype: bool
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_true(self):
        """
        Returns True if this data type evaluates to True. Returns False otherwise.

        :rtype: bool
        """
        raise NotImplementedError


# ----------------------------------------------------------------------------------------------------------------------
