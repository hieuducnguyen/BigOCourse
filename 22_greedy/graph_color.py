if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    color_list = [-1] * N
    for i in range(N):
        adjacency_color = set()
        for adjacency in graph[i]:
            if color_list[adjacency] != -1:
                adjacency_color.add(color_list[adjacency])
        for k in range(N):
            if k not in adjacency_color:
                color_list[i] = k
    print(len(set(color_list)))
