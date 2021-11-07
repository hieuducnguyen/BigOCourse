"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def printPath(s, f, path):
    if s == f:
        print(f, end=" ")
        return
    if path[s][f] == -1:
        print("No path")
        return
    printPath(s, path[s][f], path)
    print(f, end=" ")


def print_dist():
    global i, j
    print("dist matrix")
    for i in range(len(dist[0])):
        print("vertext %s" % i, end=" | ")
        for j in range(len(dist[0])):
            if i == j:
                val = 0 if dist[i][j] == 0 else "--"  ## -- là âm vô cực vì từ đỉnh A tới A có thay đổi dc dist
            else:
                val = dist[i][j] if dist[i][j] != INF else "++"  ## ++ là dương vô cực vì từ A tới B k có dist
            print("{:2}".format(val), end=" ")
        print()


def print_path():
    global i, j
    print("path matrix")
    for i in range(len(path[0])):
        print("vertext %s" % i, end=" | ")
        for j in range(len(path[0])):
            print("{:2}".format(path[i][j]), end=" ")
        print()


if __name__ == '__main__':
    V = 3
    graph = [[] for _ in range(V)]
    # vertex 0
    graph[0].append((1, -1))
    graph[0].append((2, 100))
    # vertex 1
    graph[1].append((0, -1))
    # vertex 2
    graph[2].append((1, 100))

    dist = [[INF for i in range(V)] for j in range(V)]
    path = [[-1 for i in range(V)] for j in range(V)]
    for i in range(V):
        for u, w in graph[i]:
            dist[i][u] = w
            path[i][u] = i
        if dist[i][i] == INF:
            dist[i][i] = 0
            path[i][i] = -1
    print("dist and path before run floy")
    print_dist()
    print_path()
    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF:
                continue
            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
    print("dist and path after run floy")
    print_dist()
    print_path()
