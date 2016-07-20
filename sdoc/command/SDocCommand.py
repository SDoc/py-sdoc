"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand
from sdoc.style.SdocStyle import SdocStyle


class SDocCommand(BaseCommand):
    """
    Generates the target document(s)
    """
    name = 'sdoc'

    arguments = [
        {
            'name':        'config.cfg',
            'description': 'The name of the config file',
            'required':    True
        },
        {
            'name':        'main.sdoc',
            'description': "The SDoc file",
            'required':    True
        }
    ]

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc application.
        """
        self._io = SdocStyle(self.input, self.output)

        sdoc = SDoc()
        sdoc.io = self._io
        sdoc.config_path = self.argument('config.cfg')

        return sdoc.run_sdoc(self.argument('main.sdoc'))

# ----------------------------------------------------------------------------------------------------------------------
