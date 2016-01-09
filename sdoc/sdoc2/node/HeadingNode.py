"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import CONTENT_TYPE_FLOW, CONTENT_TYPE_SECTION, CONTENT_TYPE_PALPABLE
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
    def get_content_categories(self):
        """
        Returns the content types of this node.

        :rtype: set(int)
        """
        return {CONTENT_TYPE_FLOW, CONTENT_TYPE_SECTION, CONTENT_TYPE_PALPABLE}

    # ------------------------------------------------------------------------------------------------------------------
    def get_heading_level(self):
        """
        Returns the level of the heading.

        :rtype: int
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
