from cleo.io.io import IO

from sdoc.sdoc2.formatter.Formatter import Formatter


class HtmlFormatter(Formatter):
    """
    Abstract parent class for all formatters for generating the output of nodes in HTML.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, parent: Formatter):
        """
        Object constructor.

        :param OutputStyle io: The IO object.
        :param Formatter parent: The formatter for the parent node.
        """
        Formatter.__init__(self, io, parent)

# ----------------------------------------------------------------------------------------------------------------------
