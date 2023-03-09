from cleo.helpers import argument

from sdoc.command.BaseCommand import BaseCommand
from sdoc.io.SDocIO import SDocIO
from sdoc.SDoc import SDoc


class SDoc2Command(BaseCommand):
    name = 'sdoc2'
    description = 'Parses a SDoc2 document'
    arguments = [argument('config.cfg', description='The name of the config file'),
                 argument('main.sdoc2', description='The SDoc2 document to parse')]

    # ------------------------------------------------------------------------------------------------------------------
    def _handle(self) -> int:
        """
        Reads the arguments and starts SDoc application.
        """
        sdoc = SDoc()
        sdoc.io = SDocIO(self.io.input, self.io.output, self.io.error_output)
        sdoc.config_path = self.argument('config.cfg')
        sdoc.init()

        return sdoc.run_sdoc2(self.argument('main.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
