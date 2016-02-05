"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('chapter')

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Function for generating part of the HTML document.

        :param file file: the file where we write html.
        """
        file.write("<h1>%s</h1>" % self.name)
        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            node.generate_html(file)

            node_store.out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 1.

        :rtype: int
        """
        return 1

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

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('chapter', ChapterNode)
