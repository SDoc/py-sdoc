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

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set_part_numeration(enumerable_numbers):
        """
        Sets and returns the part number. If we already haven't got a part, we set it to 1 (i.e. first part).
        If we already have part, we increment part number, and reset heading nodes numbering.

        This method changes original list with values!

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.

        :rtype: str
        """
        if 'part' not in enumerable_numbers:
            enumerable_numbers['part'] = '1'
        else:
            del enumerable_numbers['heading']
            enumerable_numbers['part'] = str(int(enumerable_numbers['part']) + 1)

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, enumerable_numbers):
        """
        Sets number of part nodes.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.
        """
        self.set_part_numeration(enumerable_numbers)
        self._options['number'] = self._trim_levels(enumerable_numbers['part'])

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            node.number(enumerable_numbers)

            out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('part', PartNode)
