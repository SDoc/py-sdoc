"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
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
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        file.write('<li>')
        self.prepare_content_tree()
        super().generate_html(file)
        file.write('</li>')

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
        if node_store.first:
            self._hierarchy_level = parent_hierarchy_level + 1
        else:
            self._hierarchy_level = parent_hierarchy_level

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
    def prepare_content_tree(self):
        """
        Method which checks if all child nodes is phrasing.
        """
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                node.prune_whitespace()

            # if not node.is_phrasing():
            #    raise RuntimeError("Node: id:%s, %s is not phrasing" % (str(node.id), node.name))

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('item', ItemNode)
