"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.ParagraphNode import ParagraphNode


class TocNode(Node):
    """
    SDoc2 node for table of contents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this table of contents.
        :param str argument: The argument of this TOC.
        """
        Node.__init__(self, io, 'toc', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node (i.e. toc).

        :rtype: str
        """
        return 'toc'

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
    def generate_toc(self):
        """
        Generates the table of contents.
        """
        self._options['ids'] = []

        for node in node_store.nodes.values():
            if not isinstance(node, ParagraphNode) and isinstance(node, HeadingNode):
                node.set_toc_id()

                data = {'id':        node.get_option_value('id'),
                        'arg':       node.argument,
                        'level':     node.get_hierarchy_level(),
                        'number':    node.get_option_value('number'),
                        'numbering': node.numbering}

                self._options['ids'].append(data)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('toc', TocNode)
