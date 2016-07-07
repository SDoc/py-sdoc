"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Application
from sdoc.command.SDoc1Command import SDoc1Command
from sdoc.command.SDoc2Command import SDoc2Command
from sdoc.command.GenerateCommand import GenerateCommand


# ----------------------------------------------------------------------------------------------------------------------
class SDoc(Application):
    """
    The SDoc application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def get_default_commands(self):
        commands = Application.get_default_commands(self)

        self.add(GenerateCommand())
        self.add(SDoc1Command())
        self.add(SDoc2Command())

        return commands

# ----------------------------------------------------------------------------------------------------------------------
