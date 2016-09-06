"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ---------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2.NodeStore import NodeStore
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class CaptionHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter stub generating HTML code for captions.
    """

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('caption', 'html', CaptionHtmlFormatter)
