"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
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
    def get_hierarchy_name(self):
        """
        Returns 'sectioning'.

        :rtype: str
        """
        return 'sectioning'

    # ------------------------------------------------------------------------------------------------------------------
    def get_enumerable_name(self):
        """
        Returns the enumerable name of this node, i.e. sectioning.

        :type: str
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
    def first_node_numerate(self, numbers):
        """
        Creates a first heading node number.

        :param dict[str,str] numbers: The number of last node.

        :rtype: str
        """
        if self.get_hierarchy_level() == 1:
            numbers['heading'] = '1'

            return numbers['heading']

        else:
            # If we start not from chapter add additional '0' for missing headers.
            arr = []
            for i in range(self.get_hierarchy_level()-1):
                arr.append('0')
            # And set '1' to the header.
            arr.append('1')

            return '.'.join(arr)

    # ------------------------------------------------------------------------------------------------------------------
    def other_nodes_numerate(self, numbers):
        """
        Creates number to all heading nodes exclude first.

        :param dict[str,str] numbers: The number of last node.

        :rtype: str
        """
        numbers_level = numbers['heading'].split('.')

        # If hierarchy level bigger than we had in numeration, add additional '0's and '1' in the
        # end to new header.
        if self.get_hierarchy_level() > len(numbers_level):
            adding = self.get_hierarchy_level() - len(numbers_level)
            for i in range(adding-1):
                numbers_level.append('0')
            numbers_level.append('1')

        # If we stays on the same level, increment number of last header number.
        elif self.get_hierarchy_level() == len(numbers_level):
            numbers_level[-1] = str(int(numbers_level[-1]) + 1)

        # Add new number of level if we returned to same level.
        else:
            numbers_level = list()
            numbers_level.append('1')

        return '.'.join(numbers_level)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def trim_levels(string_of_numbers):
        """
        Strips all starting '0's and add one starting '0' symbol if number starts from '0'.

        :param str string_of_numbers: String with header node number.

        :rtype: str
        """
        if string_of_numbers.startswith('0'):
            string_of_numbers = string_of_numbers.lstrip('0.')
            string_of_numbers = '0.%s' % string_of_numbers

        return string_of_numbers

    # ------------------------------------------------------------------------------------------------------------------
    def enumerate(self, numbers):
        """
        Sets number to heading nodes.

        :param dict[str,str] numbers: The number of last node.
        """

        # Method1 get_numeration(numbers,level)
        # if numbers['heading'] not set:
        #  get_numeration(numbers,3) => '0.0.0'
        #  get_numeration(numbers,1) => '0'

        # if numbers['heading'] is '1'
        #  get_numeration(numbers,3) => '1.0.0'
        #  get_numeration(numbers,2) => '1.0.0'
        #  get_numeration(numbers,1) => '1'

        # if numbers['heading'] is '1.2.3.4'
        #  get_numeration(numbers,3) => '1.2.3'
        #  get_numeration(numbers,2) => '1.2'
        #  get_numeration(numbers,1) => '1'

        # Method2 increment_last_level(numbers)
        # '0' => '1'
        # '1' => '2'
        # '1.0.0.0' => '1.0.0.1'
        # '1.2.3.4' => '1.2.3.4'

        if 'heading' not in numbers:
            numbers['heading'] = self.first_node_numerate(numbers)
        else:
            numbers['heading'] = self.other_nodes_numerate(numbers)

        # Set number to header.
        self._options['number'] = self.trim_levels(numbers['heading'])

        # Jump to another level.
        super().enumerate(numbers)

        # Trim numbers to get_hierarchy_level.
        numbers_level = numbers['heading'].split('.')
        numbers['heading'] = '.'.join(numbers_level[:self.get_hierarchy_level()])

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
