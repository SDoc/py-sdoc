from typing import Dict, Optional

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class IconNode(Node):
    """
    Node for icons (i.e. small inline images).
    """

    # ------------------------------------------------------------------------------------------------------------------
    _definitions = {}
    """
    The icon definitions. Map from ion name ot attributes.

    :type: dict[str,dict[str,str]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this figure.
        :param str argument: Not used.
        """
        super().__init__(io, 'icon', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e. icon.
        """
        return 'icon'

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
    def is_phrasing(self) -> bool:
        """
        Returns True if this node is a phrasing node, i.e. is a part of a paragraph. Otherwise returns False.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def add_definition(name: str, attributes: Dict[str, str]):
        """
        Adds the definition of an icon to the icon definitions.

        :param str name: The name of a reference to icon definition.
        :param dict[str,str] attributes: The attributes.
        """
        IconNode._definitions[name] = attributes

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_definition(name: str) -> Optional[Dict[str, str]]:
        """
        Returns the attributes of a definition, if name of definition is exists.

        :param str name: The name of a definition

        :rtype: dict[str,str]|None
        """
        if name in IconNode._definitions:
            return IconNode._definitions[name]
        else:
            return None


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icon', IconNode)
