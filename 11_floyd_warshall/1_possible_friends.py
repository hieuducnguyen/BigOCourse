"""
Link: https://www.spoj.com/problems/SOCIALNE/#:~:text=Two%20persons%20are%20possible%20friends,help%20him%20in%20this%20task.
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def floy_warshall(matrix):
    vertex_num = len(matrix)
    dist = [[INF for u in range(vertex_num)] for v in range(vertex_num)]
    for i in range(vertex_num):
        for j in range(vertex_num):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            if i == j:
                dist[i][i] = 0
    for k in range(vertex_num):
        for i in range(vertex_num):
            if dist[i][k] == INF:
                continue
            for j in range(vertex_num):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        matrix = []
        first_line = list(input())
        matrix.append(first_line)
        len_matrix = len(first_line)
        for k in range(len_matrix - 1):
            line = list(input())
            matrix.append(line)
        result = floy_warshall(matrix)
        max_possible_friend = 0
        max_possible_friend_id = 0
        for k in range(len_matrix):
            possible_friend = 0
            for v in range(len_matrix):
                if result[k][v] == 2:
                    possible_friend += 1
            if max_possible_friend < possible_friend:
                max_possible_friend = possible_friend
                max_possible_friend_id = k
        print(max_possible_friend_id, max_possible_friend)
