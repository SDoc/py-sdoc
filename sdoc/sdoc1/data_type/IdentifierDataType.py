from typing import Union

from sdoc.sdoc1.data_type.ArrayDataType import ArrayDataType
from sdoc.sdoc1.data_type.DataType import DataType
from sdoc.sdoc1.data_type.StringDataType import StringDataType


class IdentifierDataType(DataType):
    """
    Class for identifiers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, scope: ArrayDataType, name: Union[int, str]):
        """
        Object constructor.

        :param ArrayDataType scope: The scope of the identifier.
        :param int|str name: The name of the identifier.
        """
        self._scope: ArrayDataType = scope
        """
        The scope of this identifier.
        """

        self._name: Union[int, str] = name
        """
        The name of this identifier.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent: int = 0) -> str:
        """
        Returns a string for debugging.

        :param int indent: Unused.
        """
        if not self._scope.has_element(self._name):
            return "'{0!s}' = {1!s}".format(self._name, 'UNDEFINED')

        # Setting first indentation.
        first_indent = len("{0!s} = ".format(self._name))

        return "{0!s} = {1!s}".format(self._name, self._scope.get_reference(self._name).debug(first_indent))

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self) -> DataType:
        """
        Returns a clone of the referenced data type.
        """
        return self._scope.get_reference(self._name).dereference()

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self) -> Union[int, str]:
        """
        Returns the underling value of this data type.
        """
        return self._scope.get_reference(self._name).get_value()

    # ------------------------------------------------------------------------------------------------------------------
    def get_name(self) -> Union[int, str]:
        """
        Returns the name of this identifier.
        """
        return self._name

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self) -> int:
        """
        Returns the ID of this data type.

        :rtype: int
        """
        return self._scope.get_reference(self._name).get_type_id()

    # ------------------------------------------------------------------------------------------------------------------
    def is_constant(self) -> bool:
        """
        Returns False always.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_defined(self) -> bool:
        """
        Returns True if the reference is defined, i.e. if the element exists in the underling array. Returns False
        otherwise.
        """
        return self._scope.has_element(self._name)

    # ------------------------------------------------------------------------------------------------------------------
    def is_scalar(self) -> bool:
        """
        Returns True if this data type is a scalar. Returns False otherwise.
        """
        return bool(self._scope.get_reference(self._name).get_value())

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self) -> bool:
        """
        Returns True if this data type evaluates to True. Returns False otherwise.
        """
        return bool(self._scope.get_reference(self._name).get_value())

    # ------------------------------------------------------------------------------------------------------------------
    def get_array_element(self, key: DataType) -> DataType:
        """
        Sets the value for this identifier as an array element.

        :param DataType key: The key.
        """
        tmp = self._scope.get_array(self._name)

        return IdentifierDataType(tmp, key.get_value())

    # ------------------------------------------------------------------------------------------------------------------
    def set_value(self, value: DataType) -> DataType:
        """
        Sets the value for this identifier.

        :param DataType value: The value.
        """
        return self._scope.add_element(StringDataType(self._name), value)

# ----------------------------------------------------------------------------------------------------------------------
