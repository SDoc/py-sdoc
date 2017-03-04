"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.CaptionNode import CaptionNode
from sdoc.sdoc2.node.LabelNode import LabelNode
from sdoc.sdoc2.node.Node import Node


class FigureNode(Node):
    """
    A stub for SDoc2 node for figures.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this figure.
        """
        super().__init__(io, 'figure', options)

        self.caption = None
        """
        The caption for the figure.

        :type: None|str
        """

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
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, CaptionNode):
                self.caption = node.argument

            if isinstance(node, LabelNode):
                self.setup_label(node)

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def setup_label(self, node):
        """
        Sets the data of a label to current table.

        :param sdoc.sdoc2.node.LabelNode.LabelNode node: The label node.
        """
        self._options['id'] = node.argument

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
NodeStore.register_block_command('figure', FigureNode)
