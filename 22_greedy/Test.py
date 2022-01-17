def count_max_act(action_list, N):
    action_list.sort(key=lambda x: x[2])
    ts = 0
    result = []
    for id, start, end in action_list:
        if ts <= start:
            result.append(id)
            ts = end
    return result


if __name__ == '__main__':
    a = []
    res = []
    N = int(input())
    for i in range(N):
        start, end = map(int, input().split())
        a.append((i, start, end))
    action = count_max_act(a, N)
    print(action)
