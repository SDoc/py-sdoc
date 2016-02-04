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
    def __init__(self):
        super().__init__('item')

    # ------------------------------------------------------------------------------------------------------------------
    def gen_html(self, level, file):
        """
        Function for generating part of the HTML document.

        :param int level: the level of node.
        :param file file: the file where we write html.
        """
        file.write("<li>")
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                node.prune_whitespace()

            node.gen_html(level + 1, file)

            node_store.out_scope(node)
        file.write("</li>")

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 1.

        :rtype: int
        """
        return 1

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
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            if not node.is_phrasing():
                raise RuntimeError("Node: id:%s, %s is not phrasing" % (str(node.id), node.name))

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('item', ItemNode)
