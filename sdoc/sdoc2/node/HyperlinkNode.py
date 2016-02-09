"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from urllib import request, error
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node


class HyperlinkNode(Node):
    """
    SDoc2 node for hyperlinks.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of the hyperlink.
        :param str argument: Not used.
        """
        super().__init__('hyperlink', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_html(self, file):
        """
        Generates the HTML code for this node.

        :param file file: The output stream to with the generated HTML will be written.
        """
        file.write("<a")

        if not self._options:
            file.write(" href='%s'" % self.try_connect(self._argument))
        else:
            for key, value in self._options.items():
                if key == "href":
                    file.write(" %s='%s'" % (key, self.try_connect(value)))
                else:
                    file.write(" %s='%s'" % (key, value))

        file.write(">%s</a>" % self._argument)

    # ------------------------------------------------------------------------------------------------------------------
    def try_connect(self, url):
        """
        Tries to connect using http or https protocol. Returns a full url address.

        :param str url: The url with protocol.
        :rtype: str
        """
        # Splitting the url.
        raw_url = url.lstrip("(http://)|(https://)")

        # Trying to connect with 'https' protocol.
        try:
            request.urlopen("https://%s" % raw_url)
            return "https://%s" % raw_url
        except error.URLError:
            pass

        # Trying to connect with 'http' protocol.
        try:
            request.urlopen("http://%s" % raw_url)
            return "http://%s" % raw_url
        except error.URLError:
            return "http://%s" % raw_url
            print("Cannot connect to adress '%s'" % raw_url)

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns False.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('hyperlink', HyperlinkNode)
