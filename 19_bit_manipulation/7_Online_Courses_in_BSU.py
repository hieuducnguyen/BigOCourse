"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/12/2021
"""
import sys

sys.setrecursionlimit(10 ** 5)


def dfs(source, graph, visited, visited_list):
    if visited[source] == 2:
        return True
    if visited[source] == 1:
        return False
    visited[source] = 1
    for adjacency in graph[source]:
        if not dfs(adjacency, graph, visited, visited_list):
            return False
    visited[source] = 2
    visited_list.append(source)
    return True


if __name__ == '__main__':
    N, K = map(int, input().split())
    need_visited_list = list(map(lambda x: int(x) - 1, input().split()))
    graph = [[] for _ in range(N)]
    for n in range(N):
        num_neighbor, *neighbor_list = map(lambda x: int(x) - 1, input().split())
        for neighbor in neighbor_list:
            graph[n].append(neighbor)
    visited = [0] * N
    result = []
    for need_visit in need_visited_list:
        visited_list = []
        success = dfs(need_visit, graph, visited, visited_list)
        if not success:
            print(-1)
            exit()
        if visited_list:
            course_list = list(map(lambda x: x + 1, visited_list))
            result.extend(course_list)
    print(len(result))
    print(*result, sep=" ")
