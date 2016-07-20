"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import configparser
import os

import sys
from io import StringIO

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
    def __init__(self, styled_output):
        """
        Object contructor.
        """

        self._styled_output = styled_output
        """
        Styled output formatter.

        :type: sdoc.style.SdocStyle.SdocStyle
        """

        self._args = None
        """
        The parsed arguments of this program.

        :type: Namespace
        """

        self._formatter = None
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

        self._nodes_paths = []
        """
        A list with path names from with node modules must be imported.

        :type: [str]
        """

        self._formatter_paths = []
        """
        A list with path names from with node modules must be imported.

        :type: [str]
        """

        self._errors = 0
        """
        The total number of errors encountered at SDoc level 1 and level 2.

        :type: int
        """

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
    def set_arguments(self, config_filename, main_file):
        """
        Sets the arguments for SDoc program.
        """
        self._args = {'config_filename': config_filename,
                      'main': main_file}

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
                            .format(target_format, self._args['config_filename']))

        if not target_format:
            raise SDocError("Option 'format' in section 'sdoc' not set in config file '{0!s}'"
                            .format(self._args['config_filename']))

        # Read the class name for formatting the SDoc2 nodes into the target format.
        section = 'format_' + target_format
        class_name = config.get(section, 'class', fallback=None)
        if not class_name:
            raise SDocError("Option 'class' in section '{0!s}' not set in config file '{1!s}'".
                            format(section, self._args['config_filename']))

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
                            .format(class_name, self._args['config_filename']))

        # Create the formatter.
        self._formatter = m(config[section])

    # ------------------------------------------------------------------------------------------------------------------
    def _config_set_temp_dir(self, config):
        """
        Reads the directory for storing temporary files.

        :param configparser.ConfigParser config: The config parser.
        """
        self._temp_dir = config.get('sdoc', 'temp_dir', fallback=self._temp_dir)

        if not self._temp_dir:
            raise SDocError("Option 'temp_dir' in section 'sdoc' not set correctly in config file '{0!s}'".
                            format(self._args['config_filename']))

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
                            format(self._args['config_filename']))

        if not os.access(self._target_dir, os.W_OK):
            raise SDocError("Directory '{0!s}' is not writable".format(self._target_dir))

    # ------------------------------------------------------------------------------------------------------------------
    def _read_config_file(self):
        """
        Reads the configuration file.
        """
        config = configparser.ConfigParser()
        config.read(self._args['config_filename'])

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
        sdoc2.node_store = NodeStore(self._styled_output)

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
    def run_sdoc1(self, main_filename, temp_filename):
        """
        Run the SDoc1 parser.

        :param str main_filename: The name of the file with then main SDoc1 document.
        :param str temp_filename: The name of the temporary file where the SDoc2 document must be stored.
        """
        interpreter1 = SDoc1Interpreter(self._styled_output)
        self._errors += interpreter1.process(main_filename, temp_filename)

    # ------------------------------------------------------------------------------------------------------------------
    def run_sdoc2(self, temp_filename):
        """
        Run the SDoc2 parser.

        :param str temp_filename: The name of the temporary file where the SDoc2 document is stored.
        """
        interpreter2 = SDoc2Interpreter(self._styled_output)
        self._errors += interpreter2.process(temp_filename)

    # ------------------------------------------------------------------------------------------------------------------
    def _run_sdoc(self):
        """
        Runs the SDoc1 and SDoc2 parser.
        """
        main_filename = self._args['main']
        temp_filename = self._temp_dir + '/' + os.path.basename(main_filename) + '.sdoc2'

        self.run_sdoc1(main_filename, temp_filename)

        self.run_sdoc2(temp_filename)

        # Start generating file with specific format.
        sdoc2.node_store.generate(self._formatter)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sdoc1(self, main_filename, output_filename):
        """
        Parses a SDoc document and returns a tuple with the stdout and the resulting SDoc2 document.

        :param str main_filename: The name of the file with then main SDoc1 document.
        :param str output_filename: The name of the file which will be outputted.

        :rtype: (str,str)
        """
        self._create_node_store()
        self._import_nodes()
        self._import_formatters()

        old_stdout, sys.stdout = sys.stdout, StringIO()

        temp_filename = output_filename + '.sdoc2'
        interpreter1 = SDoc1Interpreter(self._styled_output)
        interpreter1.process(main_filename, temp_filename)

        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout

        with open(temp_filename, 'rt') as fd:
            doc2 = fd.read()

        os.unlink(temp_filename)

        return output, doc2

    # ------------------------------------------------------------------------------------------------------------------
    def test_sdoc2(self, main_filename):
        """
        Parses a SDoc document and returns a tuple with the stdout and the resulting SDoc2 document.

        :param str main_filename: The name of the file with then main SDoc1 document.

        :rtype: (str,str)
        """
        self._create_node_store()
        self._import_nodes()
        self._import_formatters()

        old_stdout, sys.stdout = sys.stdout, StringIO()

        temp_filename = main_filename + '.sdoc2'
        interpreter1 = SDoc1Interpreter(self._styled_output)
        interpreter1.process(main_filename, temp_filename)

        interpreter2 = SDoc2Interpreter(self._styled_output)
        interpreter2.process(temp_filename)

        sdoc2.node_store.number_numerable()

        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout

        with open(temp_filename, 'rt') as fd:
            doc2 = fd.read()

        os.unlink(temp_filename)

        return output, doc2

    # ------------------------------------------------------------------------------------------------------------------
    def main(self):
        """
        The main function the SDoc program.
        """
        self._read_config_file()

        self._create_node_store()

        self._import_nodes()

        self._import_formatters()

        self._run_sdoc()

        if self._errors:
            self._styled_output.writeln(" ")
            self._styled_output.writeln('There were <err>{0:d} errors</err> in total'.format(self._errors))

        exit(self._errors)

# ----------------------------------------------------------------------------------------------------------------------
