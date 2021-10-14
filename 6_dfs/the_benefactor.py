"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import sys

sys.setrecursionlimit(5 * 10 ** 4 + 5)


# def dfs(source, graph, visited):
#     stack = []
#     inner_visited = [False for _ in range(len(graph))]
#     visited[source][source] = 0
#     stack.append((source, 0))
#     while len(stack) != 0:
#         point = stack.pop()
#         inner_visited[point[0]] = True
#         for adjacency in graph[point[0]]:
#             if not inner_visited[adjacency[0]]:
#                 if visited[source][adjacency[0]] < 0:
#                     visited[source][adjacency[0]] = visited[source][point[0]] + adjacency[1]
#                     visited[adjacency[0]][source] = visited[source][adjacency[0]]
#                     stack.append((adjacency[0], visited[source][adjacency[0]]))
#                 else:
#                     stack.append((adjacency[0], visited[source][adjacency[0]]))


# def dfs(source, graph, visited, path_num):


#     visited[source] = True
#     max_path = path_num
#     for adjacency in graph[source]:
#         if not visited[adjacency[0]]:
#             max_path = max(max_path, dfs(adjacency[0], graph, visited, path_num + adjacency[1]))
#     visited[source] = False
#     return max_path


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
