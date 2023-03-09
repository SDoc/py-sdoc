from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class Sub2SectionNode(HeadingNode):
    """
    SDoc2 node for sub-subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__(io, 'sub2section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. sub2section.
        """
        return 'sub2section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 4.
        """
        return 4


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub2section', Sub2SectionNode)
NodeStore.register_inline_command('subsubsection', Sub2SectionNode)
