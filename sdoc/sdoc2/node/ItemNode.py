"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class ItemNode(Node):
    """
    SDoc2 node for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this item.
        :param str argument: Not used.
        """
        super().__init__(io, 'item', options, argument)

        self._hierarchy_level = 0
        """
        The hierarchy level of the itemize.

        :type: int
        """

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
        first = self.child_nodes[0]
        last = self.child_nodes[-1]

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                if node_id == first:
                    node.prune_whitespace(leading=True)

                elif node_id == last:
                    node.prune_whitespace(trailing=True)

                elif node_id == first and node_id == last:
                    node.prune_whitespace(leading=True, trailing=True)

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
    @staticmethod
    def strip_start_point(number):
        """
        Removes start point if it in the number.

        :param str number: The number of last node.

        :rtype: str
        """
        return number.lstrip('.')

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers):
        """
        Sets number for item nodes.

        :param dict[str,str] numbers: The number of last node.
        """
        numbers['item'] = self.strip_start_point(numbers['item'])
        numbers['item'] = self._increment_last_level(numbers['item'])

        self._options['number'] = numbers['item']

        super().number(numbers)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('item', ItemNode)
