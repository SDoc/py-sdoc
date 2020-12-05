from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.NodeStore import NodeStore


class IconDefHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter stub for definition of the Icon.
    """


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('icondef', 'html', IconDefHtmlFormatter)
