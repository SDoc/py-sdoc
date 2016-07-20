"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc


class SDoc1Command(Command):
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
        main_sdoc_file = self.argument('main.sdoc')
        output_file = self.argument('output.sdoc2')

        sdoc = SDoc()
        sdoc.test_sdoc1(main_sdoc_file, output_file)

# ----------------------------------------------------------------------------------------------------------------------
