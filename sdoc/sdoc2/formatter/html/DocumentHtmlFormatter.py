"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class DocumentHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for document node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a document node.

        :param sdoc.sdoc2.node.DocumentNode.DocumentNode node: The document node.
        :param file file: The output file.
        """
        HtmlFormatter.generate(self, node, file)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('document', 'html', DocumentHtmlFormatter)
