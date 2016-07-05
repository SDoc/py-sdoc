"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Application
from sdoc.command.GenerateCommand import GenerateCommand


# ----------------------------------------------------------------------------------------------------------------------
class SDoc(Application):
    """
    The SDoc application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def start_app(self):
        self.add(GenerateCommand())
        self.run()

# ----------------------------------------------------------------------------------------------------------------------
