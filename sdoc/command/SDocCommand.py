from cleo.helpers import argument

from sdoc.command.BaseCommand import BaseCommand
from sdoc.io.SDocIO import SDocIO
from sdoc.SDoc import SDoc


class SDocCommand(BaseCommand):
    name = 'sdoc'
    description = 'Generates the target document(s)'
    arguments = [argument('config.cfg', description='The name of the config file'),
                 argument('main.sdoc', description='The SDoc file')]

    # ------------------------------------------------------------------------------------------------------------------
    def _handle(self):
        """
        Reads the arguments and starts SDoc application.
        """
        sdoc = SDoc()
        sdoc.io = SDocIO(self.io.input, self.io.output, self.io.error_output)
        sdoc.config_path = self.argument('config.cfg')

        return sdoc.run_sdoc(self.argument('main.sdoc'))

# ----------------------------------------------------------------------------------------------------------------------
