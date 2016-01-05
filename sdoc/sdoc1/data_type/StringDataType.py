"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc1.data_type.DataType import DataType


class StringDataType(DataType):
    """
    Class for string data types.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, value):
        """
        Object constructor.

        :param str value: The value of this string constant.
        """
        self._value = value
        """
        The value of this constant integer.

        :type: string
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self):
        """
        Returns a string for debugging.

        :rtype: str
        """
        return "'" + self._value + "'"

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self):
        """
        Returns a clone of this string.

        :rtype: StringDataType
        """
        return StringDataType(self._value)

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self):
        """
        Returns the underling value of this data type.

        :rtype: str
        """
        return self._value

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
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self):
        """
        Returns True if this string is not empty. Returns False otherwise.

        :rtype: bool
        """
        return self._value != ''

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the string constant.

        :rtype: str
        """
        return self._value


# ----------------------------------------------------------------------------------------------------------------------
