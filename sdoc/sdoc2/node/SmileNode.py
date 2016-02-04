"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


class SmileNode(Node):
    """
    SDoc2 node for development testing.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('smile')

    # ------------------------------------------------------------------------------------------------------------------
    def gen_html(self, level, file):
        """
        Function for generating part of the HTML document.

        :param int level: the level of node.
        :param file file: the file where we write html.
        """
        file.write("<b>SMILE</b>")
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            node.gen_html(level, file)

            node_store.out_scope(node)

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
    def is_phrasing(self):
        """
        Returns True.

        :rtype: bool
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('smile', SmileNode)
