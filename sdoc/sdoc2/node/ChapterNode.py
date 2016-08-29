"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this chapter.
        :param str argument: The title of this chapter.
        """
        super().__init__(io, 'chapter', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. chapter.

        :rtype: str
        """
        return 'chapter'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 1.

        :rtype: int
        """
        return 1


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('chapter', ChapterNode)
