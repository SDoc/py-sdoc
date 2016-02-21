"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


class UnknownNode(Node):
    """
    SDoc2 node for development testing.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument=''):
        """
        Object constructor.

        :param dict[str,str] options: The options of this smile.
        :param str argument: Not used.
        """
        super().__init__('unknown', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        file.write('??')

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. smile.

        :rtype: str
        """
        return 'unknown'

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
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True.

        :rtype: bool
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_block_command('unknown', UnknownNode)
node_store.register_inline_command('unknown', UnknownNode)
