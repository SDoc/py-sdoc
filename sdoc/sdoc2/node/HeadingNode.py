"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.NodeStore import NodeStore, sdoc
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.node.EndParagraphNode import EndParagraphNode


class HeadingNode(Node):
    """
    Abstract class for heading nodes.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name):
        """
        Object constructor.

        :param str name: The (command) name of this node.
        """
        super().__init__(name)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self):
        """
        Returns 'sectioning'.

        :rtype: str
        """
        return 'sectioning'

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares the content tree. Create paragraph nodes.

        :rtype: None
        """
        super().prepare_content_tree()

        # Adding the id's of splitted text in 'new_child_nodes1' list.
        self.get_splitted_text_ids()

        # Creating paragraphs and add all id's in 'new_child_nodes2' list.
        self.setting_child_nodes()

    # ------------------------------------------------------------------------------------------------------------------
    def create_paragraph(self):
        """
        Method for creating paragraphs.

        :rtype: sdoc.sdoc2.node.ParagraphNode.ParagraphNode
        """
        constructor = sdoc.sdoc2.node_store.inline_creators['paragraph']
        paragraph_node = constructor()
        sdoc.sdoc2.node_store.store_node(paragraph_node)

        return paragraph_node

    # ------------------------------------------------------------------------------------------------------------------
    def get_splitted_text_ids(self):
        """
        Method for replacing text parts and creating new list of id's
        """
        new_child_nodes = []

        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, TextNode):
                list_ids = node.splitted_text()
                for ids in list_ids:
                    new_child_nodes.append(ids)
            else:
                new_child_nodes.append(node.id)

            node_store.out_scope(node)

        self.nodes = new_child_nodes

    # ------------------------------------------------------------------------------------------------------------------
    def setting_child_nodes(self):
        """
        Method for setting child nodes.
        """
        new_child_nodes = []
        paragraph_node = None

        for node_id in self.nodes:
            node = node_store.in_scope(node_id)

            if node.is_phrasing():
                if not paragraph_node:
                    paragraph_node = self.create_paragraph()
                    new_child_nodes.append(paragraph_node.id)

                paragraph_node.nodes.append(node.id)
            else:
                paragraph_node = None
                if not isinstance(node, EndParagraphNode):
                    new_child_nodes.append(node.id)

            node_store.out_scope(node)

        # Setting child nodes.
        self.nodes = new_child_nodes

# ----------------------------------------------------------------------------------------------------------------------
