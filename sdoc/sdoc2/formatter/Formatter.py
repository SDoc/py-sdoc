"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
import abc

from sdoc.sdoc2 import node_store


class Formatter:
    """
    Abstract parent class for all formatters for generating the output of nodes in a requested format.
    """
    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def generate(self, node, file):
        """
        Generates the representation of a node is the requested output format.

        :param sdoc.sdoc2.node.Node.Node node: The node for which the output must be generated.
        :param file file: The output file.
        """

        for node_id in node._child_nodes:  # @todo fix access
            child_node = node_store.in_scope(node_id)

            formatter = node_store.create_formatter(child_node.get_command(), self)
            formatter.generate(child_node, file)

            node_store.out_scope(child_node)


# ----------------------------------------------------------------------------------------------------------------------
