"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand
from sdoc.style.SdocStyle import SdocStyle


class SDocCommand(BaseCommand):
    """
    Generates the target document(s)

    sdoc
        {config.cfg : The name of the config file}
        {main.sdoc  : The SDoc file}
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

        return sdoc.run_sdoc(self.input.get_argument('main.sdoc'))

# ----------------------------------------------------------------------------------------------------------------------
