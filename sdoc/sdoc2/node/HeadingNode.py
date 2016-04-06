"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import sdoc
from sdoc.sdoc2 import in_scope, out_scope
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
    @staticmethod
    def _trim_levels(string_of_numbers):
        """
        Strips all starting '0's and add one starting '0' symbol if number starts from '0'.

        :param str string_of_numbers: String with header node number.

        :rtype: str
        """
        if string_of_numbers.startswith('0'):
            string_of_numbers = string_of_numbers.lstrip('0.')
            string_of_numbers = '0.{0!s}'.format(string_of_numbers)

        return string_of_numbers

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_numeration(enumerable_numbers, level):
        """
        Returns the current enumeration of headings at a heading level.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.
        :param int level: The level of nested heading.

        :rtype: str
        """
        if 'heading' not in enumerable_numbers:
            heading_numbers = []

            for i in range(level):
                heading_numbers.append('0')
        else:
            heading_numbers = enumerable_numbers['heading'].split('.')

            if level > len(heading_numbers):
                for num in range(level-len(heading_numbers)):
                    heading_numbers.append('0')

        return '.'.join(heading_numbers[:level])

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _increment_last_level(enumerable_numbers):
        """
        Increments the last level in number of a heading number.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.

        :rtype: str
        """
        heading_numbers = enumerable_numbers['heading'].split('.')
        heading_numbers[-1] = str(int(heading_numbers[-1]) + 1)

        return '.'.join(heading_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, enumerable_numbers):
        """
        Sets number of heading nodes.

        :param dict[str,str] enumerable_numbers: The current numbers of enumerable nodes.
        """
        enumerable_numbers['heading'] = self.get_numeration(enumerable_numbers, self.get_hierarchy_level())
        enumerable_numbers['heading'] = self._increment_last_level(enumerable_numbers)

        self._options['number'] = self._trim_levels(enumerable_numbers['heading'])

        super().number(enumerable_numbers)

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
