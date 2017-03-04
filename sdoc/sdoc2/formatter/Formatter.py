"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store, in_scope, out_scope


class Formatter:
    """
    Abstract parent class for all formatters for generating the output of nodes in a requested format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, parent):
        """
        Object constructor.

        :param cleo.styles.output_style.OutputStyle io: The IO object.
        :param sdoc.sdoc2.formatter.Formatter.Formatter parent: The formatter for the parent node.
        """
        self._io = io
        """
        The IO object.

        :type: cleo.styles.output_style.OutputStyle
        """

        self._parent = parent
        """
        The formatter for the parent node.

        :type: sdoc.sdoc2.formatter.Formatter.Formatter
        """

        self._errors = 0
        """
        The error count.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def errors(self):
        """
        Getter for the error count.

        :rtype: int
        """
        if self._parent:
            return self._parent.errors

        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def error(self, message, node=None):
        """
        Logs an error.

        :param str message: The error message.this message will be appended with 'at filename:line.column' ot the token.
        :param sdoc.sdoc2.node.Node.Node node: The node where the error occurred.
        """
        if self._parent:
            self._parent.error(message, node)
        else:
            self._errors += 1

            messages = [message]
            if node:
                filename = node.position.file_name
                line_number = node.position.start_line
                column_number = node.position.start_column + 1
                messages.append('Position: {0!s}:{1:d}.{2:d}'.format(filename, line_number, column_number))
            self._io.error(messages)

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the representation of a node in the requested output format.

        :param sdoc.sdoc2.node.Node.Node node: The node for which the output must be generated.
        :param file file: The output file.
        """
        for node_id in node.child_nodes:
            child_node = in_scope(node_id)

            formatter = node_store.create_formatter(self._io, child_node.get_command(), self)
            formatter.generate(child_node, file)

            out_scope(child_node)

# ----------------------------------------------------------------------------------------------------------------------
