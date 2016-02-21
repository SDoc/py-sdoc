"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------

from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this chapter.
        :param str argument: The title of this chapter.
        """
        super().__init__('chapter', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. chapter.

        :rtype: str
        """
        return 'chapter'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 1.

        :rtype: int
        """
        return 1

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('chapter', ChapterNode)
