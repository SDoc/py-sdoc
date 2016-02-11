"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
import abc

from sdoc.sdoc2 import node_store


class Decorator:
    """
    Abstract parent class for all decorators for generating the output of nodes in requested format.
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

            decorator = node_store.create_format_decorator(node.get_command(), self)
            decorator.generate(child_node, file)

            node_store.out_scope(child_node)


# ----------------------------------------------------------------------------------------------------------------------
