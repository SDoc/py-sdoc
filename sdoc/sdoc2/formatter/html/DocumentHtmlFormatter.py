from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.DocumentNode import DocumentNode
from sdoc.sdoc2.NodeStore import NodeStore


class DocumentHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for document node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: DocumentNode, file: Any) -> None:
        """
        Generates the HTML code for a document node.

        :param DocumentNode node: The document node.
        :param any file: The output file.
        """
        self.generate_document_node(node, file)

        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_document_node(node: DocumentNode, file: Any) -> None:
        """
        Generates the HTML code for heading node.

        :param DocumentNode node: The document node.
        :param any file: The output file.
        """
        file.write('<div class="sdoc-document-title-outer">')
        if node.title_node_id:
            title_node = in_scope(node.title_node_id)
            file.write(Html.generate_element('h1', {}, title_node.argument))
            out_scope(title_node)

        file.write('<div class="sdoc-document-title-inner">')

        if node.date_node_id:
            date_node = in_scope(node.date_node_id)
            if date_node.argument:
                file.write(Html.generate_element('span', {'class': 'sdoc-document-date'}, date_node.argument))
            out_scope(date_node)

        if node.version_node_id:
            version_node = in_scope(node.version_node_id)
            if version_node.argument:
                file.write(Html.generate_element('span', {'class': 'sdoc-document-version'}, version_node.argument))
            out_scope(version_node)

        file.write('</div>')
        file.write('</div>')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('document', 'html', DocumentHtmlFormatter)
