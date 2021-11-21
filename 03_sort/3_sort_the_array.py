"""
Link:
Time complexity: O(nlog(n))
Space complexity: O(n)
"""

def check_reverse_array():
    n = int(input())
    array = list(map(int, input().split()))
    if n == 1:
        result_pass_anyway()
        return
    sorted_array = sorted(array)
    for i in range(len(array)):
        if sorted_array[i] != array[i]:
            start = i
            end = array.index(sorted_array[i])
            break
    else:
        result_pass_anyway()
        return
    if array[start:end + 1] == sorted_array[start: end + 1][::-1] and array[end + 1:] == sorted_array[end + 1:]:
        print("yes")
        print(start + 1, end + 1)
    else:
        print("no")


def result_pass_anyway():
    print("yes")
    print(1, 1)


if __name__ == '__main__':
    check_reverse_array()
