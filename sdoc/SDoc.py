"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import configparser
import os

from sdoc import sdoc2
from sdoc.error import SDocError
from sdoc.sdoc1.SDoc1Interpreter import SDoc1Interpreter
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.SDoc2Interpreter import SDoc2Interpreter


class SDoc:
    """
    The SDoc program.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object contructor.
        """
        self._io = None
        """
        The IO object.

        :type: None|sdoc.style.SdocStyle.SdocStyle
        """

        self._format = None
        """
        The class for generation the document in the target format.

        :type: sdoc.format.Format.Format
        """

        self._target_dir = '.'
        """
        The directory where the document in the target format must be created.

        :type: str
        """

        self._temp_dir = '.'
        """
        The directory where temporary files are stored.

        :type: str
        """

        self._config_path = ''
        """
        The path of the config file.

        :type: str
        """

        self._nodes_paths = []
        """
        A list with path names from with node modules must be imported.

        :type: list[str]
        """

        self._formatter_paths = []
        """
        A list with path names from with node modules must be imported.

        :type: list[str]
        """

        self._errors = 0
        """
        The total number of errors encountered at SDoc level 1 and level 2.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def io(self):
        """
        Getter for io.

        :rtype: cleo.styles.output_style.OutputStyle
        """
        return self._io

    # ------------------------------------------------------------------------------------------------------------------
    @io.setter
    def io(self, io):
        """
        Setter for io.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        """
        self._io = io

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def config_path(self):
        """
        Getter for config_path.

        :rtype: str
        """
        return self._config_path

    # ------------------------------------------------------------------------------------------------------------------
    @config_path.setter
    def config_path(self, config_path):
        """
        Setter for config_path.

        :param cleo.styles.output_style.OutputStyle config_path: The path of the config file.
        """
        self._config_path = config_path

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def target_dir(self):
        """
        Getter for target_dir.

        :rtype: str
        """
        return self.target_dir

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def temp_dir(self):
        """
        Getter for temp_dir.

        :rtype: str
        """
        return self.temp_dir

    # ------------------------------------------------------------------------------------------------------------------
    def _config_create_formatter(self, config):
        """
        Creates the formatter for generating the document in the target format.

        :param configparser.ConfigParser config: The config parser.
        """
        available_formats = ['html']

        # Read the target format of the document.
        target_format = config.get('sdoc', 'format', fallback=None)
        if target_format not in available_formats:
            raise SDocError("The format '{0!s}' is not available in SDoc. Set another in config file '{1!s}'"
                            .format(target_format, self._config_path))

        if not target_format:
            raise SDocError("Option 'format' in section 'sdoc' not set in config file '{0!s}'"
                            .format(self._config_path))

        # Read the class name for formatting the SDoc2 nodes into the target format.
        section = 'format_' + target_format
        class_name = config.get(section, 'class', fallback=None)
        if not class_name:
            raise SDocError("Option 'class' in section '{0!s}' not set in config file '{1!s}'".
                            format(section, self._config_path))

        # Import the class.
        try:
            parts = class_name.split('.')
            module = ".".join(parts[:-1])
            __import__(module)
            m = __import__(module)
            for comp in parts[1:]:
                m = getattr(m, comp)
        except AttributeError:
            raise SDocError("There is no module named '{0!s}'! Set name correctly in config file '{1!s}'"
                            .format(class_name, self._config_path))

        # Create the formatter.
        self._format = m(self._io, target_format, config)

    # ------------------------------------------------------------------------------------------------------------------
    def _config_set_temp_dir(self, config):
        """
        Reads the directory for storing temporary files.

        :param configparser.ConfigParser config: The config parser.
        """
        self._temp_dir = config.get('sdoc', 'temp_dir', fallback=self._temp_dir)

        if not self._temp_dir:
            raise SDocError("Option 'temp_dir' in section 'sdoc' not set correctly in config file '{0!s}'".
                            format(self._config_path))

        if not os.access(self._temp_dir, os.W_OK):
            raise SDocError("Directory '{0!s}' is not writable".format(self._temp_dir))

    # ------------------------------------------------------------------------------------------------------------------
    def _config_set_target_dir(self, config):
        """
        Reads the directory where the document in the target format must be created.

        :param configparser.ConfigParser config: The config parser.
        """
        self._target_dir = config.get('sdoc', 'target_dir', fallback=self._target_dir)

        if not self._target_dir:
            raise SDocError("Option 'target_dir' in section 'sdoc' not set correctly in config file '{0!s}'".
                            format(self._config_path))

        if not os.access(self._target_dir, os.W_OK):
            raise SDocError("Directory '{0!s}' is not writable".format(self._target_dir))

    # ------------------------------------------------------------------------------------------------------------------
    def _read_config_file(self):
        """
        Reads the configuration file.
        """
        config = configparser.ConfigParser()
        config.read(self._config_path)

        # Get the temp and target directory.
        self._config_set_temp_dir(config)
        self._config_set_target_dir(config)

        # Create the formatter for generating the document in the target format.
        self._config_create_formatter(config)

        self._formatter_paths.append(os.path.dirname(__file__) + '/sdoc2/formatter')
        self._nodes_paths.append(os.path.dirname(__file__) + '/sdoc2/node')

    # ------------------------------------------------------------------------------------------------------------------
    def _create_node_store(self):
        """
        Creates the node store (for storing nodes).
        """
        sdoc2.node_store = NodeStore(self._io)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def importing(path):
        """
        Imports modules from specific path.

        :param str path: The specific path.
        """
        modules = os.listdir(os.path.dirname(__file__) + path)

        path = path.replace('/', '.')

        for module in modules:
            if module != '__init__.py' and module[-3:] == '.py':
                __import__('sdoc' + path + module[:-3], locals(), globals())

    # ------------------------------------------------------------------------------------------------------------------
    def _import_nodes(self):
        """
        Imports nodes from path which is declared below.
        """
        # @todo improve
        self.importing('/sdoc2/node/')

    # ------------------------------------------------------------------------------------------------------------------
    def _import_formatters(self):
        """
        Imports formatters from path which is declared below.
        """
        # @todo improve
        self.importing('/sdoc2/formatter/html/')

    # ------------------------------------------------------------------------------------------------------------------
    def init(self):
        """
        Executes initiations required before running SDoc.
        """
        self._read_config_file()
        self._create_node_store()
        self._import_nodes()
        self._import_formatters()

    # ------------------------------------------------------------------------------------------------------------------
    def run_sdoc1(self, sdoc1_path, sdoc2_path, log_errors=True):
        """
        Run the SDoc1 parser.

        :param str sdoc1_path: The path of the SDoc1 document.
        :param str sdoc2_path: The path were the the SDoc2 document mut be stored.
        :param bool log_errors: If true the number of errors will be logged.

        :rtype: int The count of errors.
        """
        self._io.title('SDoc1')

        interpreter1 = SDoc1Interpreter(self._io)
        self._errors += interpreter1.process(sdoc1_path, sdoc2_path)

        if log_errors and self._errors:
            self._io.writeln(" ")
            self._io.title('Errors')
            self._io.error('There were {0} errors in total'.format(self._errors))

        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def run_sdoc2(self, sdoc2_path, log_errors=True):
        """
        Run the SDoc2 parser.

        :param str sdoc2_path: The path of the SDoc2 document.
        :param bool log_errors: If true the number of errors will be logged.

        :rtype: int The count of errors.
        """
        self._io.writeln('')
        self._io.title('SDoc2')

        interpreter2 = SDoc2Interpreter(self._io)
        self._errors += interpreter2.process(sdoc2_path)

        if log_errors and self._errors:
            self._io.writeln(" ")
            self._io.title('Errors')
            self._io.error('There were {0} errors in total'.format(self._errors))

        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def run_format(self, log_errors=True):
        """
        Generates the target document in the specific format.

        :param bool log_errors: If true the number of errors will be logged.

        :rtype: int The count of errors.
        """
        self._io.writeln('')
        self._io.title('Format')

        self._errors += sdoc2.node_store.generate(self._format)

        if log_errors and self._errors:
            self._io.writeln(" ")
            self._io.title('Errors')
            self._io.error('There were {0} errors in total'.format(self._errors))

        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def run_sdoc(self, main_filename, log_errors=True):
        """
        Runs the SDoc1 and SDoc2 parser.

        :param str main_filename: The path of the SDoc1 document.
        :param bool log_errors: If true the number of errors will be logged.

        :rtype: int The count of errors.
        """
        self.init()

        temp_filename = self._temp_dir + '/' + os.path.basename(main_filename) + '.sdoc2'
        self.run_sdoc1(main_filename, temp_filename, False)
        self.run_sdoc2(temp_filename, False)
        self.run_format(False)

        if log_errors and self._errors:
            self._io.writeln(" ")
            self._io.title('Errors')
            self._io.error('There were {0} errors in total'.format(self._errors))

        return self._errors

# ----------------------------------------------------------------------------------------------------------------------
