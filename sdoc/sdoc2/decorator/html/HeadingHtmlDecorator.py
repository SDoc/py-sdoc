"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlDecorator import HtmlDecorator


class HeadingHtmlDecorator(HtmlDecorator):
    """
    HtmlDecorator for generating HTML code for headings.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        # @todo
        # file.write(Html.generate_element('h%d' % self.get_hierarchy_level(), {}, self._argument))

        # super().generate(node, file)
        pass


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_register_format_decorator('chapter', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('section', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('subsection', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('sub2section', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('sub3section', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('sub4section', 'html', HeadingHtmlDecorator)
node_store.register_register_format_decorator('sub5section', 'html', HeadingHtmlDecorator)
