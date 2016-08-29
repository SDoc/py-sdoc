"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class Sub1SectionNode(HeadingNode):
    """
    SDoc2 node for subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__(io, 'subsection', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. subsection.

        :rtype: str
        """
        return 'subsection'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 3.

        :rtype: int
        """
        return 3


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub1section', Sub1SectionNode)
NodeStore.register_inline_command('subsection', Sub1SectionNode)
