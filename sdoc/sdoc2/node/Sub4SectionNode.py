"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class Sub4SectionNode(HeadingNode):
    """
    SDoc2 node for sub-sub-sub-subsections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('sub4section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. sub4section.

        :rtype: str
        """
        return 'sub4section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 6.

        :rtype: int
        """
        return 6


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('sub4section', Sub4SectionNode)
node_store.register_inline_command('subsubsubsubsection', Sub4SectionNode)
