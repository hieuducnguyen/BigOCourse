import math

if __name__ == '__main__':
    for k in range(301):
        dup_set = set()
        value_list = []
        S = k
        for i in range(S):
            if i in dup_set:
                continue
            remain_val = int(math.sqrt(S ** 2 - i ** 2))
            if remain_val - math.sqrt(S ** 2 - i ** 2) == 0:
                dup_set.add(i)
                dup_set.add(remain_val)
                value_list.append((i, remain_val))
                value_list.append((remain_val, i))
        print(value_list)
