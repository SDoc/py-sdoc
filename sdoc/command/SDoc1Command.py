"""
SDoc
"""
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand


class SDoc1Command(BaseCommand):
    """
    Parses a SDoc1 document and generates a SDoc2 document

    sdoc1
        {main.sdoc    : The SDoc1 document to parse}
        {output.sdoc2 : The generated SDoc document}
    """

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc1 application.
        """
        sdoc = SDoc()
        sdoc.io = self.output

        return sdoc.run_sdoc1(self.input.get_argument('main.sdoc'), self.input.get_argument('output.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
