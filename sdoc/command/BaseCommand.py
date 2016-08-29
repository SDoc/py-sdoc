"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command


class BaseCommand(Command):
    """
    Abstract parent command for all out commands.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name=None):
        """
        Object constructor.

        :param str|None name: The name of the command.
        """
        Command.__init__(self, name)

        self._io = None
        """
        The IO object.

        :type: None|cleo.styles.output_style.OutputStyle
        """

# ----------------------------------------------------------------------------------------------------------------------
