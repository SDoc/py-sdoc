"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class ItemHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for an item node.

        :param sdoc.sdoc2.node.ItemNode.ItemNode node: The item node.
        :param file file: The output file.
        """
        attributes = {'id': node.get_option_value('id')}

        file.write('<li {0}>'.format(Html.generate_attribute('id', attributes['id'])))
        node.prepare_content_tree()
        HtmlFormatter.generate(self, node, file)
        file.write('</li>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('item', 'html', ItemHtmlFormatter)
