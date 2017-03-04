"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc1.data_type.DataType import DataType
from sdoc.sdoc1.data_type.StringDataType import StringDataType


class IdentifierDataType(DataType):
    """
    Class for identifiers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, scope, name):
        """
        Object constructor.

        :param sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType scope: The scope of the identifier.
        :param int|str name: The name of the identifier.
        """
        self._scope = scope
        """
        The scope of this identifier.

        :type: sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType
        """

        self._name = name
        """
        The name of this identifier.

        :type: int|str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent=0):
        """
        Returns a string for debugging.

        :param int indent: Unused.

        :rtype: str
        """
        if not self._scope.has_element(self._name):
            return "'{0!s}' = {1!s}".format(self._name, 'UNDEFINED')

        # Setting first indentation.
        first_indent = len("{0!s} = ".format(self._name))

        return "{0!s} = {1!s}".format(self._name, self._scope.get_reference(self._name).debug(first_indent))

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self):
        """
        Returns a clone of the referenced data type.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        return self._scope.get_reference(self._name).dereference()

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self):
        """
        Returns the underling value of this data type.

        :rtype: int|str
        """
        return self._scope.get_reference(self._name).get_value()

    # ------------------------------------------------------------------------------------------------------------------
    def get_name(self):
        """
        Returns the name of this identifier.

        :rtype: int|str
        """
        return self._name

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self):
        """
        Returns the ID of this data type.

        :rtype: int
        """
        return self._scope.get_reference(self._name).get_type_id()

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
        Returns True if the reference is defined, i.e. if the element exists in the underling array. Returns False
        otherwise.

        :rtype: bool
        """
        return self._scope.has_element(self._name)

    # ------------------------------------------------------------------------------------------------------------------
    def is_scalar(self):
        """
        Returns True if this data type is a scalar. Returns False otherwise.

        :rtype: bool
        """
        return self._scope.get_reference(self._name).get_value()

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self):
        """
        Returns True if this data type evaluates to True. Returns False otherwise.

        :rtype: bool
        """
        return self._scope.get_reference(self._name).get_value()

    # ------------------------------------------------------------------------------------------------------------------
    def get_array_element(self, key):
        """
        Sets the value for this identifier as an array element.

        :param sdoc.sdoc1.data_type.DataType.DataType key: The key.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        tmp = self._scope.get_array(self._name)

        return IdentifierDataType(tmp, key.get_value())

    # ------------------------------------------------------------------------------------------------------------------
    def set_value(self, value):
        """
        Sets the value for this identifier.

        :param sdoc.sdoc1.data_type.DataType.DataType value: The value.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        return self._scope.add_element(StringDataType(self._name), value)

# ----------------------------------------------------------------------------------------------------------------------
