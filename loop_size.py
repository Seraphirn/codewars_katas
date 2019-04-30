def loop_size(node):
    visited_nodes = []

    while node not in visited_nodes:
        visited_nodes.append(node)
        node = node.next()

    return len(visited_nodes) - visited_nodes.index(node)
