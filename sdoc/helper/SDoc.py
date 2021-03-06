import re


class SDoc:
    """
    Utility class with functions for generating SDoc code.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def escape(text: str) -> str:
        """
        Returns an escaped string that is safe to use in SDoc.

        :param str text: The escaped string.
        """

        def replace(match_obj):
            """
            Returns the match text prefixed with backslash

            :param re.match match_obj: The match.

            :rtype: str
            """
            return '\\' + match_obj.group(0)

        return re.sub(r'[\\{}]', replace, text)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def unescape(text: str) -> str:
        """
        Returns an unescaped SDoc escaped string. I.e. removes back slashes.

        :param str text: The SDoc escaped string.
        """

        def replace(match_obj):
            """
            Returns the match text without prefixed backslash.

            :param re.match match_obj: The match.

            :rtype: str
            """
            return match_obj.group(0)[1:]

        return re.sub(r'\\.', replace, text)

# ----------------------------------------------------------------------------------------------------------------------
