"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import html

from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class SectionNode(HeadingNode):
    """
    SDoc2 node for sections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        file.write('<h2>')
        file.write(html.escape(self._argument))
        file.write('</h2>')

        super().generate_html(file)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 2.

        :rtype: int
        """
        return 2

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('section', SectionNode)
