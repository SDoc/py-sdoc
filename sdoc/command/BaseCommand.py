"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
from cleo import Command
from cleo.styles import CleoStyle


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

    # ------------------------------------------------------------------------------------------------------------------
    def __set_style(self):
        """
        Sets the output format style used by SDoc.
        """
        # Style for file system objects (e.g. file and directory names).
        self.set_style('fso', fg='green', options=['bold'])

        # Style for errors.
        self.set_style('error', fg='red', options=['bold'])

        # Style for SDoc1 notices.
        self.set_style('notice', fg='yellow')

    # ------------------------------------------------------------------------------------------------------------------
    def execute(self, i, o):
        self.input = i
        self.output = o

        self.__set_style()
        self.output = CleoStyle(self.input, self.output)

        return self.handle()

# ----------------------------------------------------------------------------------------------------------------------
