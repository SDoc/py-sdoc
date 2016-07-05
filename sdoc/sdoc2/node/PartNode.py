"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, in_scope, out_scope
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class PartNode(HeadingNode):
    """
    SDoc2 node for parts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        PartNode constructor

        :param dict[str, str] options: The options of this part.
        :param str argument: The title of this part.
        """
        super().__init__('part', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns command of this node (i.e. 'part').

        :rtype: str
        """
        return 'part'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 0.

        :rtype: int
        """
        return 0

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('part', PartNode)
