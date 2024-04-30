import csv

def min_cable_length(graph):
    if not graph:
        return 0

    num_islands = len(graph)
    connected = [False] * num_islands
    num_edges = 0
    total_length = 0

    connected[0] = True

    while num_edges < num_islands - 1:
        min_distance = float('inf')
        start_island = 0
        end_island = 0
        for i in range(num_islands):
            if connected[i]:
                for j in range(num_islands):
                    if not connected[j] and graph[i][j]:
                        if min_distance > graph[i][j]:
                            min_distance = graph[i][j]
                            start_island = i
                            end_island = j

        total_length += graph[start_island][end_island]
        connected[end_island] = True
        num_edges += 1

    return total_length

def calculate_min_cable_length():
    graph = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]

    return min_cable_length(graph)

print(calculate_min_cable_length())
