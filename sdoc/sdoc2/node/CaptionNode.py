"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.Node import Node


class CaptionNode(Node):
    """
    SDoc2 node for captions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this caption.
        :param str argument: The title of this caption.
        """
        super().__init__(io, 'caption', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. caption.

        :rtype: str
        """
        return 'caption'

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

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('caption', CaptionNode)
