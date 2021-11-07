INF = int(1e9)
Adj = [(4, 1, 1), (3, 4, 1), (3, 3, -1), (2, 3, 1), (1, 2, 1)]
dis = [0, 0, INF, INF, INF]
V = 4
# lan1
for i in range(V - 1):
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[u] != INF and dis[v] > dis[u] + w:
            dis[v] = dis[u] + w
# lan2
for i in range(V):
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[u] != INF and dis[v] > dis[u] + w:
            dis[v] = -INF
print(dis)
