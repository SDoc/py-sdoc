"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.IconNode import IconNode
from sdoc.sdoc2.node.Node import Node


class IconDefNode(Node):
    """
    The class for definition of icons in sdoc2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this figure.
        :param str argument: Not used.
        """
        super().__init__(io, 'icon_def', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. icondef.

        :rtype: str
        """
        return 'icondef'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        reference_name = self.argument
        attributes = self._options

        IconNode.add_definition(reference_name, attributes)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icondef', IconDefNode)
