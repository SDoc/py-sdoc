"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
node_store = None
"""
The node store for SDoc2 nodes.

:type: sdoc.sdoc2.NodeStore.NodeStore
"""


# ----------------------------------------------------------------------------------------------------------------------
def in_scope(node_id):
    """
    Retrieves a node based on its ID.

    :param int node_id: The node ID.

    :rtype: sdoc.sdoc2.node.Node.Node
    """
    return node_store.nodes[node_id]


# ----------------------------------------------------------------------------------------------------------------------
def out_scope(node):
    """
    Marks a node as not longer in scope.

    :param sdoc.sdoc2.node.Node.Node node: The node.
    """
    node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
