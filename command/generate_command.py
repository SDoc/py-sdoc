"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from cleo import Command

from sdoc.SDoc import SDoc


class GenerateCommand(Command):
    """
    Class for 'generate' command.
    """

    description = 'This command starts generating output file(s).'

    name = 'generate'

    arguments = [
        {
            'name': 'config_filename',
            'description': 'The name of a config file which you want to use (e.g. config.cfg)',
            'required': True
        },
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
        config_filename = self.argument('config_filename')
        main_sdoc_file = self.argument('main_sdoc_file')

        sdoc = SDoc()
        sdoc.set_arguments(config_filename, main_sdoc_file)
        sdoc.main()

# ----------------------------------------------------------------------------------------------------------------------
