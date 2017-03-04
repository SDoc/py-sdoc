"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc1.data_type.DataType import DataType


class IntegerDataType(DataType):
    """
    Class for integer data types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, value):
        """
        Object constructor.

        :param int|str value: The value of this integer constant.
        """
        self._value = int(value)
        """
        The value of this constant integer.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent=0):
        """
        Returns a string for debugging.

        :param int indent: Unused.

        :rtype: str
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
    def get_value(self):
        """
        Returns the underling value of this data type.

        :rtype: int
        """
        return self._value

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self):
        """
        Returns the ID of this data type.

        :rtype: int
        """
        return DataType.INT

    # ------------------------------------------------------------------------------------------------------------------
    def is_constant(self):
        """
        Returns False always.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_defined(self):
        """
        Returns True always.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_scalar(self):
        """
        Returns True always.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self):
        """
        Returns True if this integer is not 0. Returns False otherwise.

        :rtype: bool
        """
        return self._value != 0

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the integer constant.

        :rtype: str
        """
        return str(self._value)

# ----------------------------------------------------------------------------------------------------------------------
