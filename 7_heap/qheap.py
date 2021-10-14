"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import bisect

if __name__ == '__main__':
    Q = int(input())
    sorted_list = []
    for _ in range(Q):
        query = input()
        if query == "3":
            print(sorted_list[0])
        else:
            opt, v = map(int, query.split())
            if opt == 1:
                bin_index = bisect.bisect(sorted_list, v)
                if bin_index < len(sorted_list) and sorted_list[bin_index] == v:
                    continue
                else:
                    sorted_list.insert(bin_index, v)
            else:
                bin_index = bisect.bisect(sorted_list, v)
                if bin_index - 1 < len(sorted_list) and sorted_list[bin_index - 1] == v:
                    sorted_list.pop(bin_index - 1)
