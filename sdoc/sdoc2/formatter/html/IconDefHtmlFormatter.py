"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class IconDefHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter stub for definition of the Icon.
    """

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('icondef', 'html', IconDefHtmlFormatter)
