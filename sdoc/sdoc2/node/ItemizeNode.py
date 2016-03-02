"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.ItemNode import ItemNode


class ItemizeNode(Node):
    """
    SDoc2 node for itemize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options):
        """
        Object constructor.

        :param dict[str,str] options: The options of this itemize.
        """
        super().__init__('itemize', options)

        self._hierarchy_level = 0

        node_store.first = True

    # ------------------------------------------------------------------------------------------------------------------
    def end_command(self):
        # do something to fix hierarchy level
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. itemize.

        :rtype: str
        """
        return 'itemize'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns parent_hierarchy_level + 1.

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
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_hierarchy_root(self):
        """
        Returns True.

        :rtype: bool
        """
        return self._hierarchy_level == 0

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Method which checks if all child nodes is instance of sdoc.sdoc2.node.ItemNode.ItemNode.
        """
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if not isinstance(node, ItemNode):
                raise RuntimeError("Node: id:%s, %s is not instance of 'ItemNode'" % (str(node.id), node.name))

            node_store.out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def level_down(self, number):
        """
        Decrements the level of hierarchy.

        :param str number: The number of last node.

        :rtype: str
        """
        number_list = number.split('.')
        number = '.'.join(number_list[:-1])

        return number

    # ------------------------------------------------------------------------------------------------------------------
    def level_up(self, numbers):
        """
        Increments the level of hierarchy.

        :param dict[str,str] numbers: The number of last node.
        """
        if 'item' in numbers:
            numbers['item'] += '.0'
        else:
            numbers['item'] = '0'

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        """
        Passing over all child nodes, for numeration.

        :param dict[str,str] numbers: The number of last node.
        """
        self.level_up(numbers)

        super().enumerate(numbers)

        numbers['item'] = self.level_down(numbers['item'])


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('itemize', ItemizeNode)
