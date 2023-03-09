from abc import ABC

from cleo.commands.command import Command


class BaseCommand(Command, ABC):
    """
    Abstract parent command for all out commands.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __set_style(self):
        """
        Sets the output format style used by SDoc.
        """
        # Style for file system objects (e.g. file and directory names).
        self.add_style('fso', fg='green', options=['bold'])

        # Style for errors.
        self.add_style('error', fg='red', options=['bold'])

        # Style for SDoc notices.
        self.add_style('notice', fg='yellow')

        # Style for titles.
        self.add_style('title', fg='yellow')

    # ------------------------------------------------------------------------------------------------------------------
    def _handle(self) -> int:
        """
        Executes this command.
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self) -> int:
        """
        Executes this command.
        """
        self.__set_style()

        return self._handle()

# ----------------------------------------------------------------------------------------------------------------------
