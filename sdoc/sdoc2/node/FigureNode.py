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
    SDoc2 node for figures.
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
    def get_enumerable_name(self):
        """
        Returns the enumerable name of this node, i.e. item.

        :type: str
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
    def _new_chapter(numbers, level):
        """
        Resets data to new chapter.

        :param dict[str,str] numbers: The number of last node.
        :param int level: The level which we need to have.
        """
        chapter = HeadingNode._get_numeration(numbers, level)

        if 'figures' not in numbers:
            numbers['figures'] = '%s.%s' % (chapter, '0')

        else:
            numbers_level = numbers['figures'].split('.')
            if chapter > numbers_level[0]:
                numbers_level[0] = chapter
                numbers_level[-1] = '0'

            numbers['figures'] = '.'.join(numbers_level)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _increment_last_level(numbers):
        """
        Increment the last level of the figure node.

        :param dict[str,str] numbers: The number of last node.
        """
        heading_numbers = numbers['figures'].split('.')
        heading_numbers[-1] = str(int(heading_numbers[-1]) + 1)

        numbers['figures'] = '.'.join(heading_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        """
        Sets number to the figure node.

        :param dict[str,str] numbers: The number of last node.
        """
        self._new_chapter(numbers, 1)
        self._increment_last_level(numbers)

        self._options['number'] = numbers['figures']

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('figure', FigureNode)
