"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class HeadingHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for headings.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        # Set id attribute to heading node.
        attributes = {'id': node.get_option_value('id')}

        text_in_tag = '{0!s}'.format(node.argument)
        file.write(Html.generate_element('h{0:d}'.format(node.get_hierarchy_level()), attributes, text_in_tag))

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('chapter', 'html', HeadingHtmlFormatter)
node_store.register_formatter('section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('subsection', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub2section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub3section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub4section', 'html', HeadingHtmlFormatter)
node_store.register_formatter('sub5section', 'html', HeadingHtmlFormatter)