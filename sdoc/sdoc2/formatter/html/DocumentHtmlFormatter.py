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
    HtmlFormatter for generating HTML code for document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a document node.

        :param sdoc.sdoc2.node.DocumentNode.DocumentNode node: The document node.
        :param file file: The output file.
        """
        file.write('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="NL" lang="NL">')
        file.write('<head><meta charset="UTF-8"/><title>sdoc</title></head>')
        file.write('<body>')

        HtmlFormatter.generate(self, node, file)

        file.write('</body>')
        file.write('</html>')
        file.close()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('document', 'html', DocumentHtmlFormatter)
