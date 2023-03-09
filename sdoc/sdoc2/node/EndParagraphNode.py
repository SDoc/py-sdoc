from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class EndParagraphNode(Node):
    """
    SDoc2 node for end of paragraphs.

    Note: End of paragraphs will are temporary used during the content tree preparation. Before and after the content
          preparation end of paragraph nodes do not exist.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: Not used.
        :param str argument: Not used.
        """
        super().__init__(io, 'end_paragraph', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. end_paragraph.

        :rtype: str
        """
        return 'end_paragraph'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Not implemented for end paragraph nodes.
        """
        raise RuntimeError()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('end_paragraph', EndParagraphNode)
