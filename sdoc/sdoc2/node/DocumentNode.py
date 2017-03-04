"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.DateNode import DateNode
from sdoc.sdoc2.node.Node import Node
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

        self.title_node_id = None
        """
        The ID of the node the title of the sdoc document.

        :type: int|None
        """

        self.date_node_id = None
        """
        The ID of the node the date of the sdoc document.

        :type: int|None
        """

        self.version_node_id = None
        """
        The ID of the node with the version of the sdoc document.

        :type: int|None
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

            node.prepare_content_tree()
            self.__set_document_info(node)

            out_scope(node)

        self.__remove_document_info_nodes()

    # ------------------------------------------------------------------------------------------------------------------
    def __set_document_info(self, node):
        """
        Sets the info of a document (i.e. date, version or title) to DocumentNode attributes.

        :param sdoc.sdoc2.node.Node.Node node: The current node.
        """
        if isinstance(node, DateNode):
            self.__check_document_info(self.date_node_id, node)
            self.date_node_id = node.id

        elif isinstance(node, TitleNode):
            self.__check_document_info(self.title_node_id, node)
            self.title_node_id = node.id

        elif isinstance(node, VersionNode):
            self.__check_document_info(self.version_node_id, node)
            self.version_node_id = node.id

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __check_document_info(info_node_current, info_node_new):
        """
        Checks if a document info node has been set already. If so, an error will be logged.

        :param int|None info_node_current: The current document info node (i.e. a property of the document).
        :param sdoc.sdoc2.node.Node.Node info_node_new: The (new) document info node.
        """
        if info_node_current:
            node = in_scope(info_node_current)
            position = node.position
            out_scope(node)

            NodeStore.error("Document info {0} can be specified only once. Previous definition at {1}.".format(
                info_node_new.name, str(position)), info_node_new)

    # ------------------------------------------------------------------------------------------------------------------
    def __remove_document_info_nodes(self):
        """
        Removes the nodes with document info from the list of child nodes.
        """
        obsolete_node_ids = [self.date_node_id, self.title_node_id, self.version_node_id]
        obsolete_node_ids = [node_id for node_id in obsolete_node_ids if node_id is not None]
        self._remove_child_nodes(obsolete_node_ids)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_block_command('document', DocumentNode)
