"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, in_scope, out_scope


class Formatter:
    """
    Abstract parent class for all formatters for generating the output of nodes in a requested format.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io):
        """
        Object constructor.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        """
        self._io = io
        """
        The IO object.

        :type cleo.styles.output_style.OutputStyle:
        """


    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the representation of a node is the requested output format.

        :param sdoc.sdoc2.node.Node.Node node: The node for which the output must be generated.
        :param file file: The output file.
        """
        for node_id in node.child_nodes:  # @todo fix access
            child_node = in_scope(node_id)

            formatter = node_store.create_formatter(self._io, child_node.get_command(), self)
            formatter.generate(child_node, file)

            out_scope(child_node)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates the representation of a node is the requested output format.

        :param sdoc.sdoc2.node.Node.Node node: The node for which the output must be generated.
        :param file file: The output file.
        """
        for node_id in node.child_nodes:  # @todo fix access
            child_node = in_scope(node_id)

            formatter = node_store.create_formatter(self._io, child_node.get_command(), self)
            formatter.generate_chapter(child_node, file)

            out_scope(child_node)

# ----------------------------------------------------------------------------------------------------------------------
