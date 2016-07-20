"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc import sdoc2
from sdoc.error import SDocError
from sdoc.format.Format import Format


class HtmlFormat(Format):
    """
    Class for generating HTML
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, config):
        """
        Object constructor.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        :param configparser.SectionProxy config: The section in the config file for the target_format.
        """
        super().__init__(io, config)

        self._enumerate = True
        """
        If set chapters, sections, etc. must be numbered.

        :type: bool
        """

        self._file_per_chapter = False
        """
        If set, will generate multiple .html files for each chapter.

        :type: bool
        """

        self._one_file = True
        """
        If set, will generate one .html file.

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

        try:
            self._file_per_chapter = config.getboolean('file_per_chapter', fallback=self._file_per_chapter)
        except ValueError:
            raise SDocError("Option 'file_per_chapter' not set correctly")

        try:
            self._one_file = config.getboolean('one_file', fallback=self._one_file)
        except ValueError:
            raise SDocError("Option 'one_file' not set correctly")

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def enumerate(self):
        """
        Getter for enumerate attribute.

        :rtype: bool
        """
        return self._enumerate

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def file_per_chapter(self):
        """
        Getter for file_per_chapter attribute.

        :rtype: bool
        """
        return self._file_per_chapter

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def one_file(self):
        """
        Getter for one_file attribute.

        :rtype: bool
        """
        return self._one_file

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self):
        """
        Starts generating HTML file.
        """
        # Activate numbering nodes.
        if self.enumerate:
            sdoc2.node_store.number_numerable()

        # Generate labels.
        sdoc2.node_store.parse_labels()

        # Generate whole HTML output file.
        if self.one_file:
            file_name = 'output.html'
            self._io.writeln('Writing <fso>{0!s}</fso>'.format(file_name))
            general_file = open(file_name, 'wt', encoding='utf8')
            formatter = sdoc2.node_store.create_formatter(self._io, 'document')
            formatter.generate(sdoc2.node_store.nodes[1], general_file)

        # Generate in mode 'output file on each chapter'.
        if self.file_per_chapter:
            formatter = sdoc2.node_store.create_formatter(self._io, 'document')
            formatter.generate_chapter(sdoc2.node_store.nodes[1], None)

# ----------------------------------------------------------------------------------------------------------------------
