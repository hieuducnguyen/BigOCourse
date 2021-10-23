"""
Link: https://www.spoj.com/problems/ABCPATH/
Time complexity: O(n)
Space complexity: O(n)
"""
alpahbet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dr = [-1, 0, 1, -1, 1, -1, 0, 1]
dc = [-1, -1, -1, 0, 0, 1, 1, 1]


def dfs(i, j, graph, status, alpahbet, visited, H, W):
    visited[i][j] = True
    max_path = status
    if graph[i][j] == alpahbet[status]:
        status += 1
        max_path += 1
        if status == len(alpahbet):
            return status
        for direct in range(8):
            new_i = i + dr[direct]
            new_j = j + dc[direct]
            if 0 <= new_i < H and 0 <= new_j < W and not visited[new_i][new_j]:
                max_path = max(max_path, dfs(new_i, new_j, graph, status, alpahbet, visited, H, W))
                if max_path == len(alpahbet):
                    return max_path
    visited[i][j] = False
    return max_path


if __name__ == '__main__':
    case = 0
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        case += 1
        graph = []
        for u in range(H):
            graph.append(list(input()))
        max_path = 0
        for i in range(H):
            for j in range(W):
                visited = [[False for u in range(W)] for v in range(H)]
                max_path = max(max_path, dfs(i, j, graph, 0, alpahbet, visited, H, W))
        print("Case %s: %s" % (case, max_path))
