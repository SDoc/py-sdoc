"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand
from sdoc.style.SdocStyle import SdocStyle


class SDoc2Command(BaseCommand):
    """
    Parses a SDoc2 document

    sdoc2
        {config.cfg : The name of the config file}
        {main.sdoc2 : The SDoc2 document to parse}
    """

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc application.
        """
        self.output = SdocStyle(self.input, self.output)

        sdoc = SDoc()
        sdoc.io = self.output
        sdoc.config_path = self.input.get_argument('config.cfg')
        sdoc.init()

        return sdoc.run_sdoc2(self.input.get_argument('main.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
