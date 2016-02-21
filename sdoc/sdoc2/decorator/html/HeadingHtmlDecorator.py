"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
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
        file.write(Html.generate_element('h%d' % node.get_hierarchy_level(), {}, node._argument))

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('chapter', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('section', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('subsection', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('sub2section', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('sub3section', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('sub4section', 'html', HeadingHtmlDecorator)
node_store.register_format_decorator('sub5section', 'html', HeadingHtmlDecorator)
