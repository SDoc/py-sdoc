"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.decorator.html.HtmlFormatter import HtmlFormatter


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

        super().generate(node, file)

        file.write('</body>')
        file.write('</html>')
        file.close()

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('document', 'html', DocumentHtmlFormatter)
