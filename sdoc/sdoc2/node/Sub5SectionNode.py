"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class Sub5SectionNode(HeadingNode):
    """
    SDoc2 node for sub-sub-sub-sub-subsections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__(io, 'sub5section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. sub5section.

        :rtype: str
        """
        return 'sub5section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 7.

        :rtype: int
        """
        return 7


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('sub5section', Sub5SectionNode)
node_store.register_inline_command('subsubsubsubsubsection', Sub5SectionNode)
