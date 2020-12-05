import abc
from typing import Union


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
    def debug(self, indent: int = 0) -> str:
        """
        Returns a string for debugging.

        :param int indent: The indentation level.
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
    def get_value(self) -> Union[int, str]:
        """
        Returns the underling value of this data type.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def get_type_id(self) -> int:
        """
        Returns the ID of this data type.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_constant(self) -> bool:
        """
        Returns True if this data type is a constant. Returns False otherwise.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_defined(self) -> bool:
        """
        Returns True if this data type is defined, i.e. has a value. Returns False otherwise.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_scalar(self) -> bool:
        """
        Returns True if this data type is a scalar. Returns False otherwise.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def is_true(self) -> bool:
        """
        Returns True if this data type evaluates to True. Returns False otherwise.
        """
        raise NotImplementedError

# ----------------------------------------------------------------------------------------------------------------------
