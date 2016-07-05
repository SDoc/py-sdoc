"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
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

        file.write('<li {}>'.format(Html.generate_attribute('id', attributes['id'])))
        node.prepare_content_tree()
        super().generate(node, file)
        file.write('</li>')

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node, file):
        """
        Generates the HTML code for an item node.

        :param sdoc.sdoc2.node.ItemNode.ItemNode node: The item node.
        :param file file: The output file.
        """
        if file:
            attributes = {'id': node.get_option_value('id')}

            file.write('<li {}>'.format(Html.generate_attribute('id', attributes['id'])))
            node.prepare_content_tree()
            super().generate_chapter(node, file)
            file.write('</li>')

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('item', 'html', ItemHtmlFormatter)
