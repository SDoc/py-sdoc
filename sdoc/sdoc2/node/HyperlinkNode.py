"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from urllib import request, error
import httplib2
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node
from sdoc.helper.Html import Html


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

        file.write(Html.generate_element('a', self.get_html_attributes(), self._argument))

    # ------------------------------------------------------------------------------------------------------------------
    def get_html_attributes(self):
        """
        Checks valid html attributes for hyperlinks and returns a list of attributes.

        :rtype: dict[str,str]
        """
        valid_html_attributes = ('href', 'class', 'id', 'download', 'hreflang', 'media', 'rel', 'target', 'type')
        attributes_dict = {}

        for key, value in self._options.items():
            if key in valid_html_attributes:
                attributes_dict[key] = value

        return attributes_dict

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self):
        """
        Prepares the content of the node. Checks url of 'href' attribute. Sets if needed.
        """
        # Setting scheme if we haven't.
        if 'href' in self._options:
            self.set_scheme(self._options['href'])
        else:
            self.set_scheme(self._argument)

        # Trying to connect
        self.try_connect()

    # ------------------------------------------------------------------------------------------------------------------
    def set_scheme(self, url):
        """
        Checks if we haven't got a scheme. Sets scheme if needed.

        :param str url: The url address with scheme or without.
        """
        if not request.urlparse(url).scheme:
            if url.startswith('ftp.'):
                url = 'ftp://%s' % url
                self._options['href'] = url
            else:
                url = 'http://%s' % url
                self._options['href'] = url

    # ------------------------------------------------------------------------------------------------------------------
    def try_connect(self):
        """
        Tries to connect to url. If have connection, checks the redirect. If redirect to 'https' protocol and
        host is the same, reset scheme in 'href' attribute.
        """
        try:
            response = request.urlopen(self._options['href'])

            # Check if we can connect to host.
            if response.getcode() not in range(200, 400):
                print("Warning! - Cannot connect to: '%s'" % self._options['href'])
            else:
                # If we connected, check the redirect.
                url = self._options['href'].lstrip('(http://)|(https://)')

                connection = httplib2.HTTPConnectionWithTimeout(url)
                connection.request('HEAD', '/')
                response = connection.getresponse()

                if response.status in range(301, 304):
                    # If host of redirected is the same, reset 'href' option
                    if response.getheader('Location').startswith('https://' + url):
                        self._options['href'].replace('http://', 'https://')
        except error.URLError:
            print("Warning! - Invalid url address: '%s'" % self._options['href'])

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
