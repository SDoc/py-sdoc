from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.IconNode import IconNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class IconDefNode(Node):
    """
    The class for definition of icons in sdoc2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this figure.
        :param str argument: Not used.
        """
        super().__init__(io, 'icon_def', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. icondef.
        """
        return 'icondef'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Prepares this node for further processing.
        """
        reference_name = self.argument
        attributes = self._options

        IconNode.add_definition(reference_name, attributes)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icondef', IconDefNode)
