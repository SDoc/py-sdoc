"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class Sub3SectionNode(HeadingNode):
    """
    SDoc2 node for sub-sub-subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__(io, 'sub3section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. sub3section.

        :rtype: str
        """
        return 'sub3section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 5.

        :rtype: int
        """
        return 5


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub3section', Sub3SectionNode)
NodeStore.register_inline_command('subsubsubsection', Sub3SectionNode)
