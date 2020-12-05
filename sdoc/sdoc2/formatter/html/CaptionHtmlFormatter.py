from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class CaptionHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter stub generating HTML code for captions.
    """


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('caption', 'html', CaptionHtmlFormatter)
