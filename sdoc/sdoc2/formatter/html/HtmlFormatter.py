"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.formatter.Formatter import Formatter


class HtmlFormatter(Formatter):
    """
    Abstract parent class for all decorators for generating the output of nodes in HTML.
    """
    def __init__(self, decorator):
        """
        Object constructor.

        :param Formatter decorator: The decorator of the parent node.
        :return:
        """
        # @todo File stuff.
        pass

# ----------------------------------------------------------------------------------------------------------------------
