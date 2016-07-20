"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc


class SDoc2Command(Command):
    """
    Parses a SDoc2 document
    """

    name = 'sdoc2'

    arguments = [
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
        main_sdoc_file = self.argument('main.sdoc2')

        sdoc = SDoc()
        sdoc.test_sdoc2(main_sdoc_file)

# ----------------------------------------------------------------------------------------------------------------------
