"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.Node import Node


class IconNode(Node):
    """
    The class for icons in sdoc2.
    """

    _definitions = {}
    """
    The static attribute with definitions of icons

    :type: dict[str, list[mixed]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of this figure.
        :param str argument: Not used.
        """
        super().__init__(io, 'icon', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. icon.

        :rtype: str
        """
        return 'icon'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def add_definition(name, attributes):
        """
        Adds definition of an icon into static attribute.

        :param str name: The name of a reference to icon definition.
        :param dict[str, list[mixed] attributes: The attributes.
        """
        IconNode._definitions[name] = attributes

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_definition(name):
        """
        Returns the attributes of a definition, if name of definition is exists.

        :param str name: The name of a definition

        :rtype: list[mixed]
        """
        if name in IconNode._definitions:
            return IconNode._definitions[name]

        else:
            return None

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icon', IconNode)
