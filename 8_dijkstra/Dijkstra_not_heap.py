INF = int(1e10)

if __name__ == '__main__':
    V = 4
    graph = [[] for _ in range(4)]
    graph[0].append((1, 1))
    graph[0].append((2, 3))
    graph[0].append((3, 5))
    graph[1].append((0, 1))
    graph[1].append((2, 1))
    graph[2].append((1, 1))
    graph[2].append((0, 3))
    graph[2].append((3, 2))
    graph[3].append((2, 2))
    graph[3].append((0, 5))
    dist = [INF for _ in range(4)]
    visited = set()
    not_visited = set()
    for i in range(4):
        not_visited.add(i)
    source = 0
    dest = 3
    dist[source] = 0
    while not_visited:  # V lần
        min_dist = INF
        min_vertex = -1
        for vertex in not_visited:
            if min_dist > dist[vertex]:
                min_dist = dist[vertex]
                min_vertex = vertex
        not_visited.remove(min_vertex)
        visited.add(min_vertex)
        for adjacency, weight in graph[min_vertex]:
            if adjacency not in visited:
                dist[adjacency] = min(dist[min_vertex] + weight, dist[adjacency])
    print(dist[dest])
