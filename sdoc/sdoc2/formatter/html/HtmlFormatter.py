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

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, parent):
        """
        Object constructor.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        :param sdoc.sdoc2.formatter.Formatter.Formatter parent: The formatter for the parent node.
        """
        Formatter.__init__(self, io, parent)

# ----------------------------------------------------------------------------------------------------------------------
