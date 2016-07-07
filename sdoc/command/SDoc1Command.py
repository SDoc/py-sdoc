"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc
from sdoc.style.SdocStyle import SdocStyle


class SDoc1Command(Command):
    """
    This command starts executing sdoc1 component.
    """

    name = 'sdoc1'

    arguments = [
        {
            'name': 'main_sdoc_file',
            'description': "The 'sdoc' file which we want to parse",
            'required': True
        },
        {
            'name': 'output_file',
            'description': "The file in which we want to output generated file",
            'required': True
        }
    ]

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc1 application.
        """
        self.output = SdocStyle(self.input, self.output)

        main_sdoc_file = self.argument('main_sdoc_file')
        output_file = self.argument('output_file')

        sdoc = SDoc(self.output)
        sdoc.test_sdoc1(main_sdoc_file, output_file)

# ----------------------------------------------------------------------------------------------------------------------
