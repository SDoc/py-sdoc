"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


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
    def check_chapter(self, numbers):
        """
        Checks the chapter. If it changes, sets numeration to '1'.

        :param dict[str,str] numbers: The number of last node.
        """

        numbers_level = numbers['heading'].split('.')
        current_figure_number = numbers['figures'].split('.')

        if numbers_level[0] > current_figure_number[0]:
            current_figure_number[0] = numbers_level[0]
            current_figure_number[-1] = '1'

        numbers['figures'] = '.'.join(current_figure_number)

    # ------------------------------------------------------------------------------------------------------------------
    def increment_number(self, numbers):
        """
        Increments number of the current figure.

        :param dict[str,str] numbers: The number of last node.
        """
        numbers_level = numbers['figures'].split('.')
        numbers_level[-1] = str(int(numbers_level[-1]) + 1)
        numbers['figures'] = '.'.join(numbers_level)

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        """
        Sets number to the figure node.

        :param dict[str,str] numbers: The number of last node.
        """
        # xxx use
        # XXX HeadingNode.get_numeration(numbers,1)

        # If we don't have figures count, create it.
        if 'figures' not in numbers:
            numbers['figures'] = '%s.%s' % (numbers['heading'].split('.')[0], '1')

        # Reset number to 1 if chapter changed.
        self.check_chapter(numbers)

        # Set number on figure node.
        self._options['number'] = numbers['figures']

        # Increment number.
        self.increment_number(numbers)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('figure', FigureNode)
