"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------


class Enumerable:
    """
    Class for storing information about numeration of heading nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """

        self._numerate_data = {}

    # ------------------------------------------------------------------------------------------------------------------
    def get_numeration(self, level):
        """
        Sets current enumeration of headings at a heading level.

        :param int level: The level of nested heading.
        """
        if not len(self._numerate_data):
            self._numerate_data[level] = 0
        else:
            if level not in self._numerate_data:
                self._numerate_data[level] = 0

        # Truncate levels.
        new_numerate_data = {}
        for key in self._numerate_data:
            if key <= level:
                new_numerate_data[key] = self._numerate_data[key]

        self._numerate_data = new_numerate_data

    # ------------------------------------------------------------------------------------------------------------------
    def increment_last_level(self):
        """
        Increments the last level in number of a heading number.
        """
        last_level = max(self._numerate_data)
        self._numerate_data[last_level] += 1

    # ------------------------------------------------------------------------------------------------------------------
    def get_string(self):
        """
        Returns the string equivalent of levels for future output.

        :rtype: str
        """
        numbering = []

        if max(self._numerate_data) == 0:
            return self._numerate_data[0]
        else:
            for key in self._numerate_data:
                # If we need to generate chapter, subsection ... etc. we omit outputting part number.
                if key != 0:
                    numbering.append(self._numerate_data[key])

            return '.'.join(map(str, numbering))

# ----------------------------------------------------------------------------------------------------------------------
