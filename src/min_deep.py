from collections import deque

def has_cycle(graph):
    for node in graph:
        visited = set()
        queue = deque([(node, None)])
        while queue:
            current_node, parent_node = queue.popleft()
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, current_node))
                elif neighbor != parent_node:
                    return True
    return False

def check_for_cycle_in_graph(graph, output_file):
    has_cycle_result = has_cycle(graph)

    with open(output_file, 'w') as file:
        if has_cycle_result:
            file.write("The graph contains a cycle.")
        else:
            file.write("The graph does not contain a cycle.")

    return has_cycle_result

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [1, 3, 5],
        3: [1, 2, 4],
        4: [3, 5],
        5: [2, 4]
    }
    result = check_for_cycle_in_graph(graph, "output.txt")
