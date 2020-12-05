from typing import Dict, Optional


class Enumerable:
    """
    Class for storing information about numeration of heading nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """

        self._numerate_data: Dict[int, int] = {}
        """
        The info about node numeration.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_level(self, level: int) -> Optional[int]:
        """
        Gets the level from numerate data.

        :param: int level: The level.
        """
        if level in self._numerate_data:
            return self._numerate_data[level]
        else:
            return None

    # ------------------------------------------------------------------------------------------------------------------
    def generate_numeration(self, level: int) -> None:
        """
        Sets current enumeration of headings at a heading level.

        :param int level: The level of nested heading.
        """
        for num in range(level + 1):
            if num not in self._numerate_data:
                self._numerate_data[num] = 0

        # Truncate levels.
        new_numerate_data = {}
        for key in self._numerate_data:
            if key <= level:
                new_numerate_data[key] = self._numerate_data[key]

        self._numerate_data = new_numerate_data

    # ------------------------------------------------------------------------------------------------------------------
    def increment_last_level(self) -> None:
        """
        Increments the last level in number of a heading number.
        """
        last_level = max(self._numerate_data)
        self._numerate_data[last_level] += 1

    # ------------------------------------------------------------------------------------------------------------------
    def remove_starting_zeros(self) -> None:
        """
        Removes starting multiple zero symbols. And lefts one if we have omitted levels.
        """
        # Check if we have level 'bigger' than part and
        # if first encountered level is equal 0, we start passing from level '2' to max level.
        if 1 in self._numerate_data and self._numerate_data[1] == 0:
            for key in range(2, max(self._numerate_data)):

                # If we have '0' we remove them until we not encountered '0', otherwise we go out the loop.
                if self._numerate_data[key] == 0:
                    del self._numerate_data[key]
                else:
                    break

    # ------------------------------------------------------------------------------------------------------------------
    def get_string(self) -> str:
        """
        Returns the string equivalent of levels for future output.
        """
        numbering = []

        if max(self._numerate_data) == 0:
            return str(self._numerate_data[0])
        else:
            for key in self._numerate_data:
                # If we need to generate chapter, subsection ... etc. we omit outputting part number.
                if key != 0:
                    numbering.append(self._numerate_data[key])

            return '.'.join(map(str, numbering))

# ----------------------------------------------------------------------------------------------------------------------
