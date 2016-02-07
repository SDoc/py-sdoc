"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
import re


# ----------------------------------------------------------------------------------------------------------------------
def escape(text):
    """
    Returns an escaped string that is svae to use in SDoc.

    :param text: The escaped string.

    :rtype: str
    """
    def replace(matchobj):
        return '\\' + matchobj.group(0)

    return re.sub(r'[\\{}]', replace, text)


# ----------------------------------------------------------------------------------------------------------------------
def unescape(text):
    """
    Returns an unescaped SDoc escaped string. I.e. removes back slashes.

    :param text: The SDoc escaped string.

    :rtype: str
    """
    def replace(matchobj):
        return matchobj.group(0)[1:]

    return re.sub(r'\\.', replace, text)

# ----------------------------------------------------------------------------------------------------------------------
