"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import re

from sdoc.sdoc2 import node_store, out_scope, in_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.ItemNode import ItemNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class ItemizeNode(Node):
    """
    SDoc2 node for itemize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this itemize.
        """
        super().__init__(io, 'itemize', options)

        self._hierarchy_level = 0
        """
        The hierarchy level of the itemize.

        :type: int
        """

        node_store.first = True

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
        Method which checks if all child nodes is instance of sdoc.sdoc2.node.ItemNode.ItemNode. If not, removes
        from child node list and from node store.
        """
        obsolete_node_ids = []

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                # Ignore text nodes with only whitespace silently.
                if re.sub(r'\s+', '', node.argument) != '':
                    # This text node contains more than only whitespace.
                    node_store.error("Unexpected text '{0}'".format(node.argument), node)
                obsolete_node_ids.append(node_id)

            elif not isinstance(node, ItemNode):
                # An itemize node can have only item nodes as direct child nodes.
                node_store.error("Node: id:{0!s}, {1!s} is not instance of 'ItemNode'".format(str(node.id), node.name),
                                 node)
                obsolete_node_ids.append(node_id)

            out_scope(node)

        self._remove_child_nodes(obsolete_node_ids)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def level_down(number):
        """
        Decrements the level of hierarchy.

        :param str number: The number of last node.

        :rtype: str
        """
        number_list = number.split('.')
        number = '.'.join(number_list[:-1])

        return number

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def level_up(numbers):
        """
        Increments the level of hierarchy.

        :param dict[str,str] numbers: The number of last node.
        """
        if 'item' in numbers:
            numbers['item'] += '.0'
        else:
            numbers['item'] = '0'

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers):
        """
        Passing over all child nodes, for numeration.

        :param dict[str,str] numbers: The number of last node.
        """
        self.level_up(numbers)

        super().number(numbers)

        numbers['item'] = self.level_down(numbers['item'])


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_block_command('itemize', ItemizeNode)
