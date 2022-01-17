def range_xor(result_list, start, end):
    return result_list[end] ^ result_list[start]


def sum_xor(result_list, start, end):
    if end - start <= 1:
        return range_xor(result_list, start, end)
    mid = (start + end) // 2
    sum_left = sum_xor(result_list, start, mid)
    sum_right = sum_xor(result_list, mid, end)
    val_mid = 0
    for i in range(start, mid):
        for j in range(mid, end):
            val_mid += range_xor(result_list, i, j + 1)
    return val_mid + sum_right + sum_left


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        result_list = [0]
        val_list = list(map(int, input().split()))
        for val in val_list:
            tmp_result = result_list[-1] ^ val
            result_list.append(tmp_result)
        #print(result_list)
        print(sum_xor(result_list, 0, N))
