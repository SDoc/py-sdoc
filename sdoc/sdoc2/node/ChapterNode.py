from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this chapter.
        :param str argument: The title of this chapter.
        """
        super().__init__(io, 'chapter', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. chapter.
        """
        return 'chapter'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 1.
        """
        return 1


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('chapter', ChapterNode)
