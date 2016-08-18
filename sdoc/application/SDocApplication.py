"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Application

from sdoc.command.SDocCommand import SDocCommand
from sdoc.command.SDoc1Command import SDoc1Command
from sdoc.command.SDoc2Command import SDoc2Command


# ----------------------------------------------------------------------------------------------------------------------
class SDocApplication(Application):
    """
    The SDocApplication application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        Application.__init__(self, 'SDocApplication', '0.0.11')

    # ------------------------------------------------------------------------------------------------------------------
    def get_default_commands(self):
        """
        Returns the default commands of this application.

        :rtype: list[cleo.Command]
        """
        commands = Application.get_default_commands(self)

        self.add(SDocCommand())
        self.add(SDoc1Command())
        self.add(SDoc2Command())

        return commands

# ----------------------------------------------------------------------------------------------------------------------
