"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import re


class SDoc:
    """
    Utility class with functions for generating SDoc code.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def escape(text):
        """
        Returns an escaped string that is svae to use in SDoc.

        :param text: The escaped string.

        :rtype: str
        """
        def replace(matchobj):
            """
            Returns the match text prefixed with backslash

            :param matchobj: The match.

            :rtype: str
            """
            return '\\' + matchobj.group(0)

        return re.sub(r'[\\{}]', replace, text)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def unescape(text):
        """
        Returns an unescaped SDoc escaped string. I.e. removes back slashes.

        :param text: The SDoc escaped string.

        :rtype: str
        """

        def replace(matchobj):
            """
            Returns the match text without prefixed backslash.

            :param matchobj: The match.

            :rtype: str
            """
            return matchobj.group(0)[1:]

        return re.sub(r'\\.', replace, text)


# ----------------------------------------------------------------------------------------------------------------------
