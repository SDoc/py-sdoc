"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand
from sdoc.style.SdocStyle import SdocStyle


class SDoc2Command(BaseCommand):
    """
    Parses a SDoc2 document
    """
    name = 'sdoc2'

    arguments = [
        {
            'name':        'config.cfg',
            'description': 'The name of the config file',
            'required':    True
        },
        {
            'name':        'main.sdoc2',
            'description': 'The SDoc2 document to parse',
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
        sdoc.init()

        return sdoc.run_sdoc2(self.argument('main.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
