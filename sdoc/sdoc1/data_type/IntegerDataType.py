from typing import Union

from sdoc.sdoc1.data_type.DataType import DataType


class IntegerDataType(DataType):
    """
    Class for integer data types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, value: Union[int, str]):
        """
        Object constructor.

        :param int|str value: The value of this integer constant.
        """
        self._value: int = int(value)
        """
        The value of this constant integer.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent: int = 0) -> str:
        """
        Returns a string for debugging.

        :param int indent: Unused.
        """
        return str(self._value)

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self):
        """
        Returns a clone of this integer.

        :rtype: sdoc.sdoc1.data_type.IntegerDataType.IntegerDataType
        """
        return IntegerDataType(self._value)

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self) -> int:
        """
        Returns the underling value of this data type.
        """
        return self._value

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self) -> int:
        """
        Returns the ID of this data type.
        """
        return DataType.INT

    # ------------------------------------------------------------------------------------------------------------------
    def is_constant(self) -> bool:
        """
        Returns False always.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_defined(self) -> bool:
        """
        Returns True always.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_scalar(self) -> bool:
        """
        Returns True always.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self) -> bool:
        """
        Returns True if this integer is not 0. Returns False otherwise.
        """
        return self._value != 0

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        """
        Returns the string representation of the integer constant.
        """
        return str(self._value)

# ----------------------------------------------------------------------------------------------------------------------
