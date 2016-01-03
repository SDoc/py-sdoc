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
        :param str name: The name of the identifier.
        """
        self._scope = scope
        """
        The scope of this identifier.

        :type: sdoc.sdoc1.data_type.ArrayDataType.ArrayDataType
        """

        self._name = name
        """
        The name of this identifier.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self):
        """
        Returns a string for debugging.

        :rtype: str
        """
        return "'%s' => %s" %(self._name, self._scope.get_reference(self._name).debug())

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self):
        """
        Returns the underling value of this data type.

        :rtype: str|int
        """
        return self._scope.get_reference(self._name).get_value()

    # ------------------------------------------------------------------------------------------------------------------
    def get_name(self):
        """
        Returns the name of this identifier.

        :rtype: str
        """
        return self._name

    # ------------------------------------------------------------------------------------------------------------------
    def is_constant(self):
        """
        Returns False always.

        :rtype: bool
        """
        return False

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
    def set_value(self, value):
        """
        Sets the value for this identifier

        :param sdoc.sdoc1.data_type.DataType.DataType value: The value.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        return self._scope.add_element(StringDataType(self._name), value)


# ----------------------------------------------------------------------------------------------------------------------
