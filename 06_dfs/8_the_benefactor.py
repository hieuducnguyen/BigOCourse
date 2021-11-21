"""
Link: https://www.spoj.com/problems/BENEFACT/
Time complexity: O(T * (V + E))
Space complexity: O(T *(V + E))
"""
import sys

sys.setrecursionlimit(5 * 10 ** 4 + 5)


def dfs(source, graph):
    stack = []
    visited = [False for _ in range(len(graph))]
    distance = [-1 for _ in range(len(graph))]
    visited[source] = True
    distance[source] = 0
    stack.append(source)
    while len(stack) != 0:
        source = stack.pop()
        for adjacency in graph[source]:
            if not visited[adjacency[0]]:
                visited[adjacency[0]] = True
                distance[adjacency[0]] = distance[source] + adjacency[1]
                stack.append(adjacency[0])
    return distance


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        vertex = int(input())
        graph = [[] for i in range(vertex)]
        for i in range(vertex - 1):
            u, v, distance = map(int, input().split())
            graph[u - 1].append((v - 1, distance))
            graph[v - 1].append((u - 1, distance))
        distance = dfs(0, graph)
        max_distance_one_source = max(distance)
        index_max_distance_one_source = distance.index(max_distance_one_source)
        distance = dfs(index_max_distance_one_source, graph)
        print(max(distance))
