"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.helper.Enumerable import Enumerable


class PartNode(HeadingNode):
    """
    SDoc2 node for parts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        PartNode constructor

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str, str] options: The options of this part.
        :param str argument: The title of this part.
        """
        super().__init__(io, 'part', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns command of this node (i.e. 'part').

        :rtype: str
        """
        return 'part'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 0.

        :rtype: int
        """
        return 0

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, enumerable_numbers):
        """
        Sets number of heading nodes.

        :param dict[str,sdoc.sdoc2.helper.Enumerable.Enumerable] enumerable_numbers:
        """
        if 'part' not in enumerable_numbers:
            enumerable_numbers['part'] = Enumerable()

        enumerable_numbers['part'].generate_numeration(self.get_hierarchy_level())
        enumerable_numbers['part'].increment_last_level()
        enumerable_numbers['part'].remove_starting_zeros()

        super().number(enumerable_numbers)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('part', PartNode)
