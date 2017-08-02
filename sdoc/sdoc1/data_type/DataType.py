"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc


class DataType(metaclass=abc.ABCMeta):
    """
    Abstract parent class for all data types.
    """

    # Constants for all data types.
    INT = 1
    STRING = 2
    ARRAY = 3

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def debug(self, indent=0):
        """
        Returns a string for debugging.

        :param int indent: The indentation level.

        :rtype: str
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def dereference(self):
        """
        Returns a clone of this data type.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
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
    def get_type_id(self):
        """
        Returns the ID of this data type.

        :rtype: int
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
    def is_defined(self):
        """
        Returns True if this data type is defined, i.e. has a value. Returns False otherwise.

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
