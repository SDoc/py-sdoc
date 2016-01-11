"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.node.Node import Node


class HeadingNode(Node):
    """
    Abstract class for heading nodes.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name):
        """
        Object constructor.

        :param str name: The (command) name of this node.
        """
        super().__init__(name)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self):
        """
        Returns 'sectioning'.

        :rtype: str
        """
        return 'sectioning'


# ----------------------------------------------------------------------------------------------------------------------
