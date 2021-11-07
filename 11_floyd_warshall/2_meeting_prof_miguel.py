"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
INF = int(1e10)


def bellman_ford(source, edge_list, num_vertex):
    dist = [INF for _ in range(num_vertex)]
    dist[source] = 0
    for i in range(num_vertex - 1):
        change = False
        for u, v, w in edge_list:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                change = True
        if not change:
            break
    return dist


if __name__ == '__main__':
    while True:
        num_street = int(input())
        if num_street == 0:
            break
        edge_list_young = []
        edge_list_old = []
        map_edge_list = {'Y': edge_list_young, 'M': edge_list_old}
        name_id_map = {}
        id_name_map = {}
        id_place = -1
        for _ in range(num_street):
            input_line = input().split()
            start = input_line[2]
            end = input_line[3]
            w = int(input_line[4])
            if start not in name_id_map:
                id_place += 1
                name_id_map[start] = id_place
                id_name_map[id_place] = start
            start_id = name_id_map[start]
            if end not in name_id_map:
                id_place += 1
                name_id_map[end] = id_place
                id_name_map[id_place] = end
            end_id = name_id_map[end]
            update_edge_list = map_edge_list[input_line[0]]
            if input_line[1] == 'U':
                update_edge_list.append((start_id, end_id, w))
            else:
                update_edge_list.append((start_id, end_id, w))
                update_edge_list.append((end_id, start_id, w))
        person_1, person_2 = input().split()
        if person_1 not in name_id_map:
            id_place += 1
            name_id_map[person_1] = id_place
            id_name_map[id_place] = person_1
        if person_2 not in name_id_map:
            id_place += 1
            name_id_map[person_2] = id_place
            id_name_map[id_place] = person_2
        dist_1 = bellman_ford(name_id_map[person_1], edge_list_young, len(name_id_map))
        dist_2 = bellman_ford(name_id_map[person_2], edge_list_old, len(name_id_map))
        result = []
        min_distance = INF
        for place_id in id_name_map:
            if dist_1[place_id] == INF or dist_2[place_id] == INF:
                continue
            if min_distance == dist_1[place_id] + dist_2[place_id]:
                result.append(id_name_map[place_id])
            elif min_distance > dist_1[place_id] + dist_2[place_id]:
                result = [id_name_map[place_id]]
                min_distance = dist_1[place_id] + dist_2[place_id]
        result.sort()
        if min_distance == INF:
            print("You will never meet.")
        else:
            print(min_distance, end=" ")
            print(*result, sep=" ")
