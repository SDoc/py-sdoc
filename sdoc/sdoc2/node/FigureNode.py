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
    def enumerate(self, numbers):
        # implement similar method get_current_enumeration
        # use heading.get_current_enumeration(1) for getting chapter number
        # if first level different => restart from 1
        # else increment

        # If we don't have figures count, create it.
        if 'figures' not in numbers:
            numbers['figures'] = 1

        # Set number on figure node.
        chapter = numbers['sectioning'].split('.')[0]
        self._options['number'] = chapter + '.' + str(numbers['figures'])

        # Increment number.
        numbers['figures'] += 1

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('figure', FigureNode)
