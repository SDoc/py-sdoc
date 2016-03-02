"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.formatter.Formatter import Formatter


class HtmlFormatter(Formatter):
    """
    Abstract parent class for all formatters for generating the output of nodes in HTML.
    """
    def __init__(self, formatter):
        """
        Object constructor.

        :param Formatter formatter: The formatter of the parent node.
        """
        # @todo File stuff.
        pass

# ----------------------------------------------------------------------------------------------------------------------
