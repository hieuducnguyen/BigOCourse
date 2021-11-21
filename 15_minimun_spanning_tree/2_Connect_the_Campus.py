"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1338
Time complexity: O(T * N^2 * Log(N)) E: num edge = N(N-1)/2
Space complexity: O(N^2)
Author: Nguyen Duc Hieu
"""
import heapq

import math

INF = int(1e10)


def distance(first_point, second_point):
    return math.sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)


def prim(matrix):
    V = len(matrix)
    visited = [False] * V
    dist = [INF] * V
    dist[0] = 0
    min_heap = [(0, 0)]
    while min_heap:
        weight_source, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for i in range(N):
            adjacency, weight = i, matrix[source][i]
            if not visited[adjacency] and dist[adjacency] > weight:
                heapq.heappush(min_heap, (weight, adjacency))
                dist[adjacency] = weight
    return dist


if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            matrix = [[INF] * N for _ in range(N)]
            point_list = []
            for n in range(N):
                X, Y = map(int, input().split())
                point_list.append((X, Y))
            M = int(input())
            for m in range(M):
                A, B = map(lambda x: int(x) - 1, input().split())
                matrix[A][B] = 0
                matrix[B][A] = 0
            for i in range(N):
                for j in range(i + 1, N):
                    if matrix[i][j] == INF:
                        matrix[i][j] = matrix[j][i] = distance(point_list[i], point_list[j])
            dist = prim(matrix)
            print("{:.2f}".format(sum(dist)))
        except EOFError:
            exit()
