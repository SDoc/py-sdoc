"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


class LabelNode(Node):
    """
    SDoc2 node for labels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this label.
        :param str argument: The title of this label.
        """
        super().__init__('label', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. label.

        :rtype: str
        """
        return 'label'

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
node_store.register_inline_command('label', LabelNode)
