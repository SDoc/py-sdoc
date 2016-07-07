"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc
from sdoc.style.SdocStyle import SdocStyle


class SDoc2Command(Command):
    """
    This command starts executing sdoc2 component.
    """

    name = 'sdoc2'

    arguments = [
        {
            'name': 'main_sdoc_file',
            'description': "The 'sdoc' file which we want to parse",
            'required': True
        }
    ]

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc application.
        """
        self.output = SdocStyle(self.input, self.output)

        main_sdoc_file = self.argument('main_sdoc_file')

        sdoc = SDoc(self.output)
        sdoc.test_sdoc2(main_sdoc_file)

# ----------------------------------------------------------------------------------------------------------------------
