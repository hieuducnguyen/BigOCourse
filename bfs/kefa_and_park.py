"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue


def bfs(V, graph, cat_list, C):
    if V == 1:
        return 1 if cat_list[0] < C else 0
    q = Queue()
    visited = [False for _ in range(V)]
    visited[0] = True
    q.put((0, cat_list[0]))
    num_restaurant = 0
    while q.qsize() != 0:
        point = q.get()
        if len(graph[point[0]]) == 1 and point[0] != 0:
            num_restaurant += 1
        else:
            for adjacency in graph[point[0]]:
                if not visited[adjacency]:
                    visited[adjacency] = True
                    if cat_list[adjacency] == 1:
                        if point[1] + cat_list[adjacency] <= C:
                            q.put((adjacency, point[1] + cat_list[adjacency]))
                    else:
                        q.put((adjacency, 0))
    return num_restaurant


if __name__ == '__main__':
    V, C = map(int, input().split())
    cat_list = list(map(int, input().split()))
    graph = [[] for _ in range(V)]
    for _ in range(V - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    print(bfs(V, graph, cat_list, C))
