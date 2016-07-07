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
    'This command starts executing SDoc app and generating output file(s).'
    """

    name = 'generate'

    arguments = [
        {
            'name': 'config_file',
            'description': 'The name of a config file which you want to use (e.g. config.cfg)',
            'required': True
        },
        {
            'name': 'main_sdoc_file',
            'description': "The SDoc file which we want to parse",
            'required': True
        }
    ]

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Reads the arguments and starts SDoc application.
        """
        self.output = SdocStyle(self.input, self.output)

        config_filename = self.argument('config_file')
        main_sdoc_file = self.argument('main_sdoc_file')

        sdoc = SDoc(self.output)
        sdoc.set_arguments(config_filename, main_sdoc_file)
        sdoc.main()

# ----------------------------------------------------------------------------------------------------------------------
