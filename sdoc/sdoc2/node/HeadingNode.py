"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import sdoc
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.helper.Enumerable import Enumerable
from sdoc.sdoc2.node.EndParagraphNode import EndParagraphNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode


class HeadingNode(Node):
    """
    Abstract class for heading nodes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, name, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param str name: The (command) name of this heading.
        :param dict[str,str] options: The options of this heading.
        :param str argument: The title of this heading.
        """
        super().__init__(io, name, options, argument)

        self.numbering = True
        """
        The True the node must be numbered.

        :type: bool
        """

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
    def number(self, enumerable_numbers):
        """
        Sets number of heading nodes.

        :param dict[str,sdoc.sdoc2.helper.Enumerable.Enumerable] enumerable_numbers:
        """
        if 'heading' not in enumerable_numbers:
            enumerable_numbers['heading'] = Enumerable()

        enumerable_numbers['heading'].generate_numeration(self.get_hierarchy_level())
        enumerable_numbers['heading'].increment_last_level()
        enumerable_numbers['heading'].remove_starting_zeros()

        if 'part' in enumerable_numbers:
            self._options['part_number'] = enumerable_numbers['part'].get_string()

        self._options['number'] = enumerable_numbers['heading'].get_string()

        super().number(enumerable_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def set_toc_id(self):
        """
        Set ID for table of contents.
        """
        if 'id' not in self._options:
            if 'part_number' in self._options:
                self._options['id'] = '{}:{}:{}'.format(self.name,
                                                        self._options['part_number'],
                                                        self._options['number'])
            else:
                self._options['id'] = '{}:{}'.format(self.name, self._options['number'])

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares the content tree. Create paragraph nodes.
        """
        super().prepare_content_tree()

        self.set_numbering()

        # Adding the id's of splitted text in 'new_child_nodes1' list.
        self.split_text_nodes()

        # Creating paragraphs and add all id's in 'new_child_nodes2' list.
        self.create_paragraphs()

    # ------------------------------------------------------------------------------------------------------------------
    def set_numbering(self):
        """
        Sets the numbering status to the heading node.
        """
        if 'numbering' in self._options:
            if self._options['numbering'] == 'off':
                self.numbering = False
            elif self._options['numbering'] == 'on':
                self.numbering = True
            else:
                NodeStore.error("Invalid value '{}' for attribute 'numbering'. Allowed values are 'on' and 'off'.".
                                format(self._options['numbering']), self)

    # ------------------------------------------------------------------------------------------------------------------
    def split_text_nodes(self):
        """
        Replaces single text nodes that contains a paragraph separator (i.e. a double new line) with multiple text nodes
        without paragraph separator.
        """
        new_child_nodes = []

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                list_ids = node.split_by_paragraph()
                for ids in list_ids:
                    new_child_nodes.append(ids)
            else:
                new_child_nodes.append(node.id)

            out_scope(node)

        self.child_nodes = new_child_nodes

    # ------------------------------------------------------------------------------------------------------------------
    def create_paragraphs(self):
        """
        Create paragraph nodes.

        A paragraph consists of phrasing nodes only. Each continuous slice of phrasing child nodes is move to a
        paragraph node.
        """
        new_child_nodes = []
        paragraph_node = None

        for node_id in self.child_nodes:
            node = in_scope(node_id)

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

            out_scope(node)

        if paragraph_node:
            paragraph_node.prune_whitespace()
            sdoc.sdoc2.node_store.store_node(paragraph_node)
            # paragraph_node = None

        # Setting child nodes.
        self.child_nodes = new_child_nodes

# ----------------------------------------------------------------------------------------------------------------------
