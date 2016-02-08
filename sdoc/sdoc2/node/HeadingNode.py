"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from html import escape
import sdoc
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.node.EndParagraphNode import EndParagraphNode


class HeadingNode(Node):
    """
    Abstract class for heading nodes.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name, options, argument):
        """
        Object constructor.

        :param str name: The (command) name of this heading.
        :param dict[str,str] options: The options of this heading.
        :param str argument: The title of this heading.
        """
        super().__init__(name, options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        level = str(self.get_hierarchy_level())
        file.write('<h%s>' % level)
        file.write(escape(self._argument))
        file.write('</h%s>' % level)

        super().generate_html(file)

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
        Returns 'sectioning'.

        :rtype: str
        """
        return 'sectioning'

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
        Prepares the content tree. Create paragraph nodes.
        """
        super().prepare_content_tree()

        # Adding the id's of splitted text in 'new_child_nodes1' list.
        self.split_text_nodes()

        # Creating paragraphs and add all id's in 'new_child_nodes2' list.
        self.create_paragraphs()

    # ------------------------------------------------------------------------------------------------------------------
    def split_text_nodes(self):
        """
        Replaces single text nodes that contains a paragraph separator (i.e. a double new line) with multiple text nodes
        without paragraph separator.
        """
        new_child_nodes = []

        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                list_ids = node.split_by_paragraph()
                for ids in list_ids:
                    new_child_nodes.append(ids)
            else:
                new_child_nodes.append(node.id)

            node_store.out_scope(node)

        self._child_nodes = new_child_nodes

    # ------------------------------------------------------------------------------------------------------------------
    def create_paragraphs(self):
        """
        Create paragraph nodes.

        A paragraph consists of phrasing nodes only. Each continuous slice of phrasing child nodes is move to a
        paragraph node.
        """
        new_child_nodes = []
        paragraph_node = None

        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if node.is_phrasing():
                if not paragraph_node:
                    paragraph_node = sdoc.sdoc2.node_store.create_inline_node('paragraph')
                    new_child_nodes.append(paragraph_node.id)

                paragraph_node.append_child_node(node)
            else:
                if paragraph_node:
                    paragraph_node.prune_whitespace()
                    sdoc.sdoc2.node_store.store_node(paragraph_node)
                    paragraph_node = None

                # End paragraph nodes are created temporary to separate paragraphs in a flat list of (text) node. There
                # role ae replaced by the content hierarchy now. So, we must no store end paragraph nodes.
                if not isinstance(node, EndParagraphNode):
                    new_child_nodes.append(node.id)

            node_store.out_scope(node)

        if paragraph_node:
            paragraph_node.prune_whitespace()
            sdoc.sdoc2.node_store.store_node(paragraph_node)
            # paragraph_node = None

        # Setting child nodes.
        self._child_nodes = new_child_nodes

# ----------------------------------------------------------------------------------------------------------------------
