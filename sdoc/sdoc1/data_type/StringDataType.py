from sdoc.sdoc1.data_type.DataType import DataType


class StringDataType(DataType):
    """
    Class for string data types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, value: str):
        """
        Object constructor.

        :param str value: The value of this string constant.
        """
        self._value: str = value
        """
        The value of this constant integer.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent: int = 0) -> str:
        """
        Returns a string for debugging.

        :param int indent: Unused.
        """
        return "'" + self._value + "'"

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self):
        """
        Returns a clone of this string.

        :rtype: sdoc.sdoc1.data_type.StringDataType.StringDataType
        """
        return StringDataType(self._value)

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self) -> str:
        """
        Returns the underling value of this data type.
        """
        return self._value

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self) -> int:
        """
        Returns the ID of this data type.
        """
        return DataType.STRING

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
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self) -> bool:
        """
        Returns True if this string is not empty. Returns False otherwise.
        """
        return self._value != ''

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        """
        Returns the string representation of the string constant.
        """
        return self._value

# ----------------------------------------------------------------------------------------------------------------------
