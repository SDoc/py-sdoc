from cleo.helpers import argument

from sdoc.command.BaseCommand import BaseCommand
from sdoc.io.SDocIO import SDocIO
from sdoc.SDoc import SDoc


class SDoc1Command(BaseCommand):
    name = 'sdoc1'
    description = 'Parses a SDoc1 document and generates a SDoc2 document'
    arguments = [argument('main.sdoc', description='The SDoc1 document to parse'),
                 argument('output.sdoc2', description='The generated SDoc document')]

    # ------------------------------------------------------------------------------------------------------------------
    def _handle(self) -> int:
        """
        Reads the arguments and starts SDoc1 application.
        """
        sdoc = SDoc()
        sdoc.io = SDocIO(self.io.input, self.io.output, self.io.error_output)

        return sdoc.run_sdoc1(self.argument('main.sdoc'), self.argument('output.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
