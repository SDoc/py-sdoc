from typing import Any, Dict

from cleo.io.io import IO

from sdoc.sdoc2.helper.Enumerable import Enumerable
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class PartNode(HeadingNode):
    """
    SDoc2 node for parts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        PartNode constructor

        :param OutputStyle io: The IO object.
        :param dict[str, str] options: The options of this part.
        :param str argument: The title of this part.
        """
        super().__init__(io, 'part', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns command of this node (i.e. 'part').
        """
        return 'part'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 0.
        """
        return 0

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, enumerable_numbers: Dict[str, Any]) -> None:
        """
        Sets number of heading nodes.

        :param dict[str,any] enumerable_numbers:
        """
        if 'part' not in enumerable_numbers:
            enumerable_numbers['part'] = Enumerable()

        enumerable_numbers['part'].generate_numeration(self.get_hierarchy_level())
        enumerable_numbers['part'].increment_last_level()
        enumerable_numbers['part'].remove_starting_zeros()

        super().number(enumerable_numbers)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('part', PartNode)
