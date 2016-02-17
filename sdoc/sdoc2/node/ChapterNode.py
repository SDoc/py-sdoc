"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------

from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.SectionNode import SectionNode


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

    # ------------------------------------------------------------------------------------------------------------------
    def set_numbers(self, level):
        """
        Sets numbers to section nodes.

        :param str level: The level of hierarchy.
        """
        self._options['number'] = level

        number = 1
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, SectionNode):
                node.set_numbers(self._options['number'] + '.' + str(number))
                number += 1

            node_store.out_scope(node)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('chapter', ChapterNode)
