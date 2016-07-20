"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.SDoc import SDoc
from sdoc.command.BaseCommand import BaseCommand
from sdoc.style.SdocStyle import SdocStyle


class SDoc1Command(BaseCommand):
    """
    Parses a SDoc1 document and generates a SDoc2 document
    """
    name = 'sdoc1'

    arguments = [
        {
            'name':        'main.sdoc',
            'description': 'The SDoc1 document to parse',
            'required':    True
        },
        {
            'name':        'output.sdoc2',
            'description': 'The generated SDoc document',
            'required':    True
        }
    ]

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc1 application.
        """
        self._io = SdocStyle(self.input, self.output)

        sdoc = SDoc()
        sdoc.io = self._io

        return sdoc.run_sdoc1(self.argument('main.sdoc'), self.argument('output.sdoc2'))

# ----------------------------------------------------------------------------------------------------------------------
