"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.error import SDocError
from sdoc.format.Format import Format


class HtmlFormat(Format):
    """
    Class for generating HTML
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, config):
        """
        Object constructor.

        :param configparser.SectionProxy config: The section in the config file for the target_format.
        """
        super().__init__(config)

        self._enumerate = True
        """
        If set chapters, sections, etc. must be numbered.

        :type: bool
        """

        self._read_configuration(config)

    # ------------------------------------------------------------------------------------------------------------------
    def _read_configuration(self, config):
        """
        Reads the configuration for this formatter.

        :param configparser.SectionProxy config: The section in the config file for the target_format.
        """
        try:
            self._enumerate = config.getboolean('enumerate', fallback=self._enumerate)

        except ValueError:
            raise SDocError("Option 'enumerate' not set correctly")

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self):
        pass

# ----------------------------------------------------------------------------------------------------------------------
