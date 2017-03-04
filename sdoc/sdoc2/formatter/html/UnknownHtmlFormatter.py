"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class UnknownHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for unknown SDoc2 node types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for an unknown node.

        :param sdoc.sdoc2.node.Node.Node node: The unknown node.
        :param file file: The output file.
        """
        self.write_into_file(node)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates the HTML code for an unknown node.

        :param sdoc.sdoc2.node.Node.Node node: The unknown node.
        :param file file: The output file.
        """
        if file:
            self.write_into_file(node)

    # ------------------------------------------------------------------------------------------------------------------
    def write_into_file(self, node):
        """
        Writes into opened file.

        :param sdoc.sdoc2.node.Node.Node node: The unknown node.
        """
        self.error('Unknown SDoc2 command {0}'.format(node.name), node)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('unknown', 'html', UnknownHtmlFormatter)
