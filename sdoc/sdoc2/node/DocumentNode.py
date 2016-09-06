"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.DateNode import DateNode
from sdoc.sdoc2.node.TitleNode import TitleNode
from sdoc.sdoc2.node.VersionNode import VersionNode


class DocumentNode(Node):
    """
    SDoc2 node for documents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this document.
        """
        super().__init__(io, 'document', options)

        self.title_node = None
        """
        The title of the sdoc document.

        :type: int
        """

        self.date_node = None
        """
        The date of the sdoc document.

        :type: int
        """

        self.version_node = None
        """
        The version of the sdoc document.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. document.

        :rtype: str
        """
        return 'document'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level=-1):
        """
        Returns 0.

        :rtype: int
        """
        return 0

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
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_document_root(self):
        """
        Returns True.
        :rtype: bool
        """
        return True

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
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares this node for further processing.
        """
        for node_id in self.child_nodes:
            node = in_scope(node_id)

            self.setup_document_info(node)
            node.prepare_content_tree()

            out_scope(node)

        self.remove_nodes_from_child()

    # ------------------------------------------------------------------------------------------------------------------
    def setup_document_info(self, node):
        """
        Sets the info of a document (i.e. date, version or title) to DocumentNode attributes.

        :param sdoc.sdoc2.node.Node.Node node: The current node.
        """
        if isinstance(node, DateNode):
            self.check_attr(self.date_node, node)
            self.date_node = node.id

        elif isinstance(node, TitleNode):
            self.check_attr(self.title_node, node)
            self.title_node = node.id

        elif isinstance(node, VersionNode):
            self.check_attr(self.version_node, node)
            self.version_node = node.id

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def check_attr(attr, node):
        """
        Checks if attribute is set. If it set, and we want to set it again, we raise an error.

        :param sdoc.sdoc2.node.Node.Node attr: The attribute which we check.
        :param sdoc.sdoc2.node.Node.Node node: The node which we want to set.
        """
        if attr:
            NodeStore.error("There are more than 1 {}'s are set. Please Fix it.".format(node.name))

    # ------------------------------------------------------------------------------------------------------------------
    def remove_nodes_from_child(self):
        """
        Removes the node from a child list node.
        """
        for node_id in (self.date_node, self.title_node, self.version_node):
            if node_id:
                self.child_nodes.remove(node_id)

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_block_command('document', DocumentNode)
