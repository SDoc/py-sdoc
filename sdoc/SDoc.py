"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import argparse
import configparser
import os

import sys
from io import StringIO

import sdoc
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
    def _parse_arguments(self):
        """
        Parses the arguments for SDoc program.
        """
        parser = argparse.ArgumentParser(description='Description')

        parser.add_argument(metavar='[main.sdoc]',
                            nargs=1,
                            dest='main',
                            help='path to main SDoc document')

        parser.add_argument('-c',
                            '--config',
                            metavar='<config.cfg>',
                            required=True,
                            dest='config_filename',
                            help='path to configuration file')

        parser.add_argument('-1',
                            '--sdoc1-only',
                            action='store_true',
                            dest='sdoc1-only',
                            default=False,
                            help='runs only the SDoc1 parser')

        self._args = parser.parse_args()

    # ------------------------------------------------------------------------------------------------------------------
    def _config_create_formatter(self, config):
        """
        Creates the formatter for generating the document in the target format.

        :param configparser.ConfigParser config: The config parser.
        """
        # Read the target format of the document.
        target_format = config.get('sdoc', 'format', fallback=None)
        if not target_format:
            raise SDocError("Option 'format' in section 'sdoc' not set in config file '{0!s}'".format(
                            self._args.config_filename))

        # Read the class name for formatting the SDoc2 nodes into the target format.
        section = 'format_' + target_format
        class_name = config.get(section, 'class', fallback=None)
        if not class_name:
            raise SDocError("Option 'class' in section '{0!s}' not set in config file '{1!s}'".format(section, self._args.config_filename))

        # Import the class.
        parts = class_name.split('.')
        module = ".".join(parts[:-1])
        __import__(module)
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)

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
            raise SDocError("Option 'temp_dir' in section 'sdoc' not set correctly in config file '{0!s}'".format(
                            self._args.config_filename))

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
            raise SDocError("Option 'target_dir' in section 'sdoc' not set correctly in config file '{0!s}'".format(
                            self._args.config_filename))

        if not os.access(self._target_dir, os.W_OK):
            raise SDocError("Directory '{0!s}' is not writable".format(self._target_dir))

    # ------------------------------------------------------------------------------------------------------------------
    def _read_config_file(self):
        """
        Reads the configuration file.
        """
        config = configparser.ConfigParser()
        config.read(self._args.config_filename)

        # Get the temp and target directory.
        self._config_set_temp_dir(config)
        self._config_set_target_dir(config)

        # Create the formatter for generating the document in the target format.
        self._config_create_formatter(config)

        self._formatter_paths.append(os.path.dirname(__file__) + '/sdoc2/formatter')
        self._nodes_paths.append(os.path.dirname(__file__) + '/sdoc2/node')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _create_node_store():
        """
        Creates the node store (for storing nodes).
        """
        sdoc.sdoc2.node_store = NodeStore()

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
        # @todo improve
        self.importing('/sdoc2/node/')

    # ------------------------------------------------------------------------------------------------------------------
    def _import_formatters(self):
        # @todo improve
        self.importing('/sdoc2/formatter/html/')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def run_sdoc1(main_filename, temp_filename):
        """
        Run the SDoc1 parser.

        :param str main_filename: The name of the file with then main SDoc1 document.
        :param str temp_filename: The name of the temporary file where the SDoc2 document must be stored.
        """
        interpreter1 = SDoc1Interpreter()
        interpreter1.process(main_filename, temp_filename)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def run_sdoc2(temp_filename):
        """
        Run the SDoc2 parser.

        :param str temp_filename: The name of the temporary file where the SDoc2 document is stored.
        """
        interpreter2 = SDoc2Interpreter()
        interpreter2.process(temp_filename)
        sdoc.sdoc2.node_store.generate()

    # ------------------------------------------------------------------------------------------------------------------
    def _run_sdoc(self):
        """
        Runs the SDoc1 and SDoc2 parser.
        """
        main_filename = self._args.main[0]
        temp_filename = self._temp_dir + '/' + os.path.basename(main_filename) + '.sdoc2'

        self.run_sdoc1(main_filename, temp_filename)

        self.run_sdoc2(temp_filename)

        sdoc.sdoc2.node_store.generate()

    # ------------------------------------------------------------------------------------------------------------------
    def test_sdoc1(self, main_filename):
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
        interpreter1 = SDoc1Interpreter()
        interpreter1.process(main_filename, temp_filename)

        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout

        fd = open(temp_filename, 'rt')
        sdoc2 = fd.read()
        fd.close()

        os.unlink(temp_filename)

        return output, sdoc2

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
        interpreter1 = SDoc1Interpreter()
        interpreter1.process(main_filename, temp_filename)

        interpreter2 = SDoc2Interpreter()
        interpreter2.process(temp_filename)

        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout

        fd = open(temp_filename, 'rt')
        sdoc2 = fd.read()
        fd.close()

        os.unlink(temp_filename)

        return output, sdoc2

    # ------------------------------------------------------------------------------------------------------------------
    def main(self):
        """
        The main function the SDoc program.
        """
        try:
            self._parse_arguments()

            self._read_config_file()

            self._create_node_store()

            self._import_nodes()

            self._import_formatters()

            self._run_sdoc()

            exit(0)

        except RuntimeError as err:
            print(err)
            exit(-1)

# ----------------------------------------------------------------------------------------------------------------------
