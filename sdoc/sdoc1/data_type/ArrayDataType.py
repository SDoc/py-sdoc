"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import copy
from sdoc.sdoc1.data_type.DataType import DataType


class ArrayDataType(DataType):
    """
    Class for array data types.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self._elements = {}
        """
        The elements in this array.

        :type: dict[mixed, sdoc.sdoc1.data_type.DataType.DataType]
        """

    # ------------------------------------------------------------------------------------------------------------------
    def debug(self, indent=0):
        """
        Returns a string for debugging.

        :rtype: str
        """
        ret = ''
        sep = " => "
        longest = 0
        counter = 0

        # cheking the longest key
        for (key, value) in self._elements.items():
            if len("%s" % key) >= longest:
                longest = len("%s" % key)
                # need this check, because every quote it's an additional symbol
                if isinstance(key, str):
                    longest += 2

        for (key, value) in self._elements.items():
            # setting first indentation
            if counter == 0:
                indentation = 0
            else:
                indentation = indent

            # checking the key type, and setting quotes
            if isinstance(key, int):
                str1 = " " * indentation + "{}".format(key).ljust(longest, " ")
            if isinstance(key, str):
                str1 = " " * indentation + "'{}'".format(key).ljust(longest, " ")

            # creating indentation level
            if isinstance(value, ArrayDataType):
                # need this check if we have many nested nodes
                if counter == 0:
                    indent += len(str1 + sep)
                else:
                    indent = len(str1 + sep)
                str2 = "{}".format(value.debug(indent)).ljust(longest, " ")
                ret += str1 + sep + str2
            else:
                str2 = "{}".format(value.debug()).ljust(longest, " ")
                ret += str1 + sep + str2 + "\n"
            counter += 1

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def dereference(self):
        """
        Returns a clone of this array.

        :rtype: ArrayDataType
        """
        tmp = ArrayDataType()
        tmp._elements = copy.deepcopy(self._elements)

        return tmp

    # ------------------------------------------------------------------------------------------------------------------
    def get_array(self, key):
        """
        Adds a new elements to this array. If the key holds an element already the element will be replaced.

        :param int_str key: The key of the new element. Must be a scalar data type.

        :rtype: sdoc.sdoc1.data_type.DataType.ArrayDataType

        @todo consider key must be int or str
        """
        if key not in self._elements:
            # Variable is not defined: create a new array.
            self._elements[key] = ArrayDataType()

        else:
            # Variable is defined.
            element = self._elements[key]
            if not isinstance(element, ArrayDataType):
                # Variable is defined but not an array: replace the element.
                self._elements[key] = ArrayDataType()

        return self._elements[key]

    # ------------------------------------------------------------------------------------------------------------------
    def add_element(self, key, value):
        """
        Adds a new elements to this array. If the key holds an element already the element will be replaced.

        :param sdoc.sdoc1.data_type.DataType.DataType key: The key of the new element. Must be a scalar data type.
        :param sdoc.sdoc1.data_type.DataType.DataType value: The value of the new element.

        :rtype: sdoc.sdoc1.data_type.DataType.DataType

        @todo consider key must be int or str
        """
        if not key.is_scalar():
            raise RuntimeError("Key '%s' is not a scalar." % str(key))

        self._elements[key.get_value()] = value.dereference()

        return self._elements[key.get_value()]

    # ------------------------------------------------------------------------------------------------------------------
    def get_reference(self, name):
        """
        Returns a reference to an element in this array.

        :param int|str name: The name of the elements

        :rtype: sdoc.sdoc1.data_type.DataType.DataType
        """
        if name not in self._elements:
            raise RuntimeError("Identifier '%s' does not have a value." % name)

        return self._elements[name]

    # ------------------------------------------------------------------------------------------------------------------
    def get_value(self):
        """
        Not implemented.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    def get_type_id(self):
        """
        Returns the ID of this data type.

        :rtype: int
        """
        return DataType.ARRAY

    # ------------------------------------------------------------------------------------------------------------------
    def has_element(self, name):
        """
        Returns True if this array has a specified element.

        :param int|str name: The name of the element.

        :rtype: bool
        """
        return name in self._elements

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
        Returns False always.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_true(self):
        """
        Returns True if this array holds 1 or more elements. Returns False otherwise.

        :rtype: bool
        """
        return len(self._elements) > 0

# ----------------------------------------------------------------------------------------------------------------------
