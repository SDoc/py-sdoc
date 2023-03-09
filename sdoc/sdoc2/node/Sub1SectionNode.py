from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class Sub1SectionNode(HeadingNode):
    """
    SDoc2 node for subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__(io, 'subsection', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. subsection.
        """
        return 'subsection'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 3.
        """
        return 3


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub1section', Sub1SectionNode)
NodeStore.register_inline_command('subsection', Sub1SectionNode)
