##
# We'll use the strategy we outlined above:

# Identify a node with no incoming edges.
# Add that node to the ordering.
# Remove it from the graph.
# Repeat.


def topological_sort(digraph):
    # digraph is a dictionary:
    #   key: a node
    # value: a set of adjacent neighboring nodes

    # construct a dictionary mapping nodes to their
    # indegrees
    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for neighbor in digraph[node]:
            indegrees[neighbor] += 1

    # track nodes with no incoming edges
    nodes_with_no_incoming_edges = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)

    # initially, no nodes in our ordering
    topological_ordering = []

    # as long as there are nodes with no incoming edges
    # that can be added to the ordering
    while len(nodes_with_no_incoming_edges) > 0:
        # add one of those nodes to the ordering
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)

        # decrement the indegree of that node's neighbors
        for neighbor in digraph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_incoming_edges.append(neighbor)

    # we've run out of nodes with no incoming edges
    # did we add all the nodes or find a cycle?
    if len(topological_ordering) == len(digraph):
        return topological_ordering  # got them all
    else:
        raise Exception("Graph has a cycle! No topological ordering exists.")


# Time and Space Complexity
# Determine the indegree for each node. This is O(M) time (where M is the number of edges),
# since this involves looking at each directed edge in the graph once.
# Find nodes with no incoming edges.
# This is a simple loop through all the nodes with some number of constant-time appends.
# O(N) time (where N is the number of nodes).
#
# Add nodes until we run out of nodes with no incoming edges. This loop could run once for every node—
# O(N) times. In the body, we:
# Do two constant-time operations on a list to add a node to the topological ordering.
# Decrement the indegree for each neighbor of the node we added. Over the entire algorithm, we'll end up doing exactly one decrement for each edge, making this step
# O(M) time overall.

# All together the time complexity is O(M+N)
# Space complexity: O(N)
