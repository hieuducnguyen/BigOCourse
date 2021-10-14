"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

dc = [-1, -1, -1, 0, 0, 1, 1, 1]
dr = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(i, j, graph, visited, status, param, R, C):
    visited[i][j] = True
    if graph[i][j] == param[status]:
        status += 1
        if status == len(param):
            return True
        for _ in range(8):
            new_i = i + dr[_]
            new_j = j + dc[_]
            if 0 <= new_i < R and 0 <= new_j < C and not visited[new_i][new_j]:
                if dfs(new_i, new_j, graph, visited, status, param, R, C):
                    return True
    visited[i][j] = False
    return False


def check_well():
    # text_check = "ALLIZZWELL"
    text_check = "ALLIZZWELL"
    R, C = map(int, input().split())
    graph = []
    for i in range(R):
        graph.append(list(input()))
    if R * C < len(text_check):
        return False
    visited = [[False for u in range(C)] for v in range(R)]
    for i in range(R):
        for j in range(C):
            if dfs(i, j, graph, visited, 0, text_check, R, C):
                return True
    return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        found = check_well()
        if found:
            print("YES")
        else:
            print("NO")
        if _ != T - 1:
            input()
