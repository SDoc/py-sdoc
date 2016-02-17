"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Sub3SectionNode import Sub3SectionNode


class Sub2SectionNode(HeadingNode):
    """
    SDoc2 node for sub-subsections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('sub2section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. sub2section.

        :rtype: str
        """
        return 'sub2section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 4.

        :rtype: int
        """
        return 4

    # ------------------------------------------------------------------------------------------------------------------
    def set_numbers(self, level):
        """
        Sets numbers to sub-sub-subsection nodes.

        :param str level: The level of hierarchy.
        """
        self._options['number'] = level

        number = 1
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, Sub3SectionNode):
                node.set_numbers(self._options['number'] + '.' + str(number))
                number += 1

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('sub2section', Sub2SectionNode)
node_store.register_inline_command('subsubsection', Sub2SectionNode)
