"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, in_scope, out_scope
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class ItemNode(Node):
    """
    SDoc2 node for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this item.
        :param str argument: Not used.
        """
        super().__init__('item', options, argument)

        self._hierarchy_level = 0

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. item.

        :rtype: str
        """
        return 'item'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns parent_hierarchy_level.

        :param int parent_hierarchy_level: The level of the parent in the hierarchy.

        :rtype: int
        """
        self._hierarchy_level = parent_hierarchy_level + 1

        return self._hierarchy_level

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self):
        """
        Returns 'item'

        :rtype: str
        """
        return 'item'

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
    def is_list_element(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Method which checks if all child nodes is phrasing.
        """
        for node_id in self._child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                node.prune_whitespace()

            # if not node.is_phrasing():
            #    raise RuntimeError("Node: id:%s, %s is not phrasing" % (str(node.id), node.name))

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _increment_last_level(number):
        """
        Increments the last level in number of the item node.

        :param str number: The number of last node.

        :rtype: str
        """
        heading_numbers = number.split('.')
        heading_numbers[-1] = str(int(heading_numbers[-1]) + 1)

        return '.'.join(heading_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def strip_start_point(self, number):
        """
        Removes start point if it in the number.

        :param str number: The number of last node.

        :rtype: str
        """
        return number.lstrip('.')

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        """
        Sets number for item nodes.

        :param dict[str,str] numbers: The number of last node.
        """
        numbers['item'] = self.strip_start_point(numbers['item'])
        numbers['item'] = self._increment_last_level(numbers['item'])

        self._options['number'] = numbers['item']

        super().enumerate(numbers)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('item', ItemNode)
