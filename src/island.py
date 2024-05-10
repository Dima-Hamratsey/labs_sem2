INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)

    dist = [[0] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
            if i != j and dist[i][j] < INF:
                pred[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


def print_shortest_paths(dist, pred):
    n = len(dist)
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == INF:
                print(f"INF detected between {i} and {j}")


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph = []
        total_sum = 0
        for line in file:
            row = list(map(int, line.strip().split(';')))
            graph.append(row)
            total_sum += sum(row)
        return [[value // 2 for value in row] for row in graph], total_sum // 2


def main():
    filename = 'data.csv'
    graph, total_sum = read_graph_from_file(filename)
    dist, pred = floyd_warshall(graph)
    print_shortest_paths(dist, pred)
    print("Total sum of INF in the graph:", total_sum)


if __name__ == "__main__":
    main()
