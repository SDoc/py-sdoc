from cleo.application import Application

from sdoc.command.SDoc1Command import SDoc1Command
from sdoc.command.SDoc2Command import SDoc2Command
from sdoc.command.SDocCommand import SDocCommand


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
        Application.__init__(self, 'SDoc', '1.0.0')

        self.add(SDocCommand())
        self.add(SDoc1Command())
        self.add(SDoc2Command())

# ----------------------------------------------------------------------------------------------------------------------
