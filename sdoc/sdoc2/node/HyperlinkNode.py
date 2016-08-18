"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from urllib import request, error

import httplib2

from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.node.Node import Node


class HyperlinkNode(Node):
    """
    SDoc2 node for hyperlinks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, options, argument):
        """
        Object constructor.

        :param None|cleo.styles.output_style.OutputStyle io: The IO object.
        :param dict[str,str] options: The options of the hyperlink.
        :param str argument: Not used.
        """
        super().__init__(io, 'hyperlink', options, argument)

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
                url = 'ftp://{0!s}'.format(url)
                self._options['href'] = url
            else:
                url = 'http://{0!s}'.format(url)
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
                self.io.warning("Cannot connect to: '{0!s}'".format(self._options['href']))
            else:
                # If we connected, check the redirect.
                url = self._options['href'].lstrip('(http://)|(https://)')
                splitted_url = url.split('/')

                host = splitted_url[0]
                address = '/'.join(splitted_url[1:])

                connection = httplib2.HTTPConnectionWithTimeout(host)
                connection.request('HEAD', address)
                response = connection.getresponse()

                if response.status in range(301, 304):
                    # If host of redirected is the same, reset 'href' option
                    if response.getheader('Location').startswith('https://' + url):
                        self._options['href'].replace('http://', 'https://')

        except error.URLError:
            self.io.warning("Invalid url address: '{0!s}'".format(self._options['href']))

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. hyperlink.

        :rtype: str
        """
        return 'hyperlink'

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True.

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
NodeStore.register_inline_command('hyperlink', HyperlinkNode)
