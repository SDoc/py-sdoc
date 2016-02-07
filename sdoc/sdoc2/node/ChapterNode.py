"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import html

from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this chapter.
        :param str argument: The title of this chapter.
        """
        super().__init__('chapter', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        file.write('<h1>')
        file.write(html.escape(self._argument))
        file.write('</h1>')

        super().generate_html(file)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 1.

        :rtype: int
        """
        return 1


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('chapter', ChapterNode)
