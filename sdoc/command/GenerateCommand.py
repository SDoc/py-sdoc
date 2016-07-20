"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc
from sdoc.style.SdocStyle import SdocStyle


class GenerateCommand(Command):
    """
    Generates the target document(s)
    """

    name = 'generate'

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
        self.output = SdocStyle(self.input, self.output)

        config_filename = self.argument('config.cfg')
        main_sdoc_file = self.argument('main.sdoc')

        sdoc = SDoc(self.output)
        sdoc.set_arguments(config_filename, main_sdoc_file)
        sdoc.main()

# ----------------------------------------------------------------------------------------------------------------------
