"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 20/02/2022
"""
import math


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.len_num = len(nums)
        height = int(math.ceil(math.log2(2 * self.len_num - 1)))
        self.segment_tree = [-1] * max(1, 2 ** height - 1)
        self.build_tree(self.segment_tree, 0, 0, self.len_num - 1, nums)

    def update(self, pos, val):
        self.updateRecursively(self.segment_tree, 0, 0, self.len_num - 1, pos, val)

    def build_tree(self, segment_tree, index, left, right, nums):
        if left == right:
            segment_tree[index] = nums[left]
            return
        mid = left + (right - left) // 2
        self.build_tree(segment_tree, 2 * index + 1, left, mid, nums)
        self.build_tree(segment_tree, 2 * index + 2, mid + 1, right, nums)
        segment_tree[index] = segment_tree[2 * index + 1] + segment_tree[2 * index + 2]

    def updateRecursively(self, segment_tree, index, left, right, pos, val):
        if right < pos or left > pos:
            return
        if left == right:
            self.segment_tree[index] = val
            return
        mid = left + (right - left) // 2
        self.updateRecursively(segment_tree, 2 * index + 1, left, mid, pos, val)
        self.updateRecursively(segment_tree, 2 * index + 2, mid + 1, right, pos, val)
        segment_tree[index] = segment_tree[2 * index + 1] + segment_tree[2 * index + 2]

    def sum(self, from_index, to_index):
        return self.sumRecursively(self.segment_tree, 0, 0, self.len_num - 1, from_index, to_index)

    def sumRecursively(self, segment_tree, index, left, right, from_index, to_index):
        if from_index <= left and right <= to_index:
            return segment_tree[index]
        if to_index < left or from_index > right:
            return 0
        mid = left + (right - left) // 2
        return self.sumRecursively(segment_tree, 2 * index + 1, left, mid, from_index, to_index) + self.sumRecursively(
            segment_tree, 2 * index + 2, mid + 1, right, from_index, to_index)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, Q = map(int, input().split())
        nums = list(map(int, input().split()))
        segment_tree = SegmentTree(nums)
        print("Case {}:".format(t + 1))
        for q in range(Q):
            query_string = input()
            if query_string[:1] == "1":
                operation_str, ind_str = query_string.split()
                index = int(ind_str)
                print(nums[index])
                nums[index] = 0
                segment_tree.update(index, 0)
            elif query_string[:1] == "2":
                operation, i, v = map(int, query_string.split())
                nums[i] += v
                segment_tree.update(i, nums[i])
            else:
                operation, i, j = map(int, query_string.split())
                print(segment_tree.sum(i, j))
