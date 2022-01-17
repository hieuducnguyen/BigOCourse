def check(row, col, tmp_result, matrix):
    for i in range(row):
        if tmp_result[i][col] > 0:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if tmp_result[i][j] > 0:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < 8:
        if tmp_result[i][j] > 0:
            return False
        i -= 1
        j += 1
    return True


def count_max(matrix, k, tmp_result, result):
    if k == 8:
        tmp_sum = 0
        for row in range(8):
            tmp_sum += sum(tmp_result[row])
        result.append(tmp_sum)
        return
    for i in range(8):
        if check(k, i, tmp_result, matrix):
            tmp_result[k][i] = matrix[k][i]
            count_max(matrix, k + 1, tmp_result, result)
            tmp_result[k][i] = 0


def count_max_pos(matrix):
    tmp_result = [[0] * 8 for _ in range(8)]
    result = []
    count_max(matrix, 0, tmp_result, result)
    return max(result)


if __name__ == '__main__':
    K = int(input())
    result = []
    for k in range(K):
        matrix = []
        for i in range(8):
            input_item = list(input().split())
            input_list = []
            for val in input_item:
                if val != " ":
                    input_list.append(int(val))
            matrix.append(input_list)
        result.append(count_max_pos(matrix))
    for val in result:
        print("{:5d}".format(val), end="")
    print()
