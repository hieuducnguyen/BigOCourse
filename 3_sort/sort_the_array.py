"""
Link:
Time complexity: O(nlog(n))
Space complexity: O(n)
"""


# def check_reverse_array():
#     n = int(input())
#     array = list(map(int, input().split()))
#     if n == 1:
#         print("yes")
#         print(1, 1)
#         return
#     num_reverse = 0
#     is_reverse = False
#     start, end = -1, len(array)
#     for i in range(len(array)):
#         if i == 0:
#             if array[0] > array[1]:
#                 num_reverse += 1
#                 start = 0
#                 is_reverse = not is_reverse
#         elif not is_reverse and array[i] < array[i - 1]:
#             num_reverse += 1
#             end, start = update_start_end(end, i, start)
#             is_reverse = not is_reverse
#         elif is_reverse and array[i] > array[i - 1]:
#             num_reverse += 1
#             end, start = update_start_end(end, i, start)
#             is_reverse = not is_reverse
#         if num_reverse > 2:
#             break
#     if num_reverse > 2 or (end < len(array) and array[start] > array[end]):
#         print("no")
#     else:
#         print("yes")
#         print(start + 1, end)
# 
# 
# def update_start_end(end, i, start):
#     if start >= 0:
#         end = i
#     else:
#         start = i
#     return end, start


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
