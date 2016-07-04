"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class FigureNode(Node):
    """
    A stub for SDoc2 node for figures.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this figure.
        :param str argument: Not used.
        """
        super().__init__('figure', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. smile.

        :rtype: str
        """
        return 'figure'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _get_numeration(enumerable_numbers):
        """
        Returns the current enumeration of figures.

        :param dict[str, sdoc.sdoc2.helper.Enumerable.Enumerable] enumerable_numbers:
        """
        if 'heading' in enumerable_numbers and enumerable_numbers['heading'].get_level(1):
            chapter = enumerable_numbers['heading'].get_level(1)
        else:
            chapter = 0

        if 'figures' not in enumerable_numbers:
            enumerable_numbers['figures'] = '{0!s}.{1!s}'.format(chapter, '0')

        else:
            numbers_level = enumerable_numbers['figures'].split('.')
            if chapter > int(numbers_level[0]):
                numbers_level[0] = chapter
                numbers_level[-1] = '0'

            enumerable_numbers['figures'] = '.'.join(map(str, numbers_level))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _increment_last_level(enumerable_numbers):
        """
        Increments the last level of figures enumeration.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.
        """
        heading_numbers = enumerable_numbers['figures'].split('.')
        heading_numbers[-1] = str(int(heading_numbers[-1]) + 1)

        enumerable_numbers['figures'] = '.'.join(heading_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, enumerable_numbers):
        """
        Sets the number of this figure node.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.
        """
        self._get_numeration(enumerable_numbers)
        self._increment_last_level(enumerable_numbers)

        self._options['number'] = enumerable_numbers['figures']

        super().number(enumerable_numbers)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('figure', FigureNode)
