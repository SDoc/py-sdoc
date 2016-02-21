"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class Sub1SectionNode(HeadingNode):
    """
    SDoc2 node for subsections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('subsection', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. subsection.

        :rtype: str
        """
        return 'subsection'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 3.

        :rtype: int
        """
        return 3


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('sub1section', Sub1SectionNode)
node_store.register_inline_command('subsection', Sub1SectionNode)
