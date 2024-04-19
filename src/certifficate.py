from collections import deque

def build_dependency_graph(file_path):
    dependencies = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            dependency, document = line.strip().split()
            if document not in dependencies:
                dependencies[document] = []
            dependencies[document].append(dependency)
            if dependency not in dependencies:
                dependencies[dependency] = []
    return dependencies

def topological_sort(dependencies):
    in_degree = {node: 0 for node in dependencies}
    for dependencies_list in dependencies.values():
        for node in dependencies_list:
            in_degree[node] += 1
    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    result = []
    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        if current_node in dependencies:
            for neighbor in dependencies[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    return result

def write_sorted_documents(sorted_documents, file_path):
    with open(file_path, 'w') as file:
        for document in sorted_documents:
            file.write(document + '\n')

file_path_in = 'govern.in'
file_path_out = 'govern.out'

dependencies = build_dependency_graph(file_path_in)
sorted_documents = topological_sort(dependencies)
write_sorted_documents(sorted_documents, file_path_out)
