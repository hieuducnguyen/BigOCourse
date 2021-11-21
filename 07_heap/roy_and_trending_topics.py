"""
Link: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/
Time complexity: O(N * log(5) + 5 * log(5))
Space complexity: O(N)
"""
import heapq


class EntryTopic:
    def __init__(self, id, change_score, new_score):
        self.id = id
        self.change_score = change_score
        self.new_score = new_score

    def __lt__(self, other):
        if self.change_score == other.change_score:
            return self.id < other.id
        return self.change_score < other.change_score


if __name__ == '__main__':
    N = int(input())
    heap = []
    for _ in range(N):
        id, old_zcore, mention, like, comment, share = map(int, input().split())
        new_score = mention * 50 + like * 5 + comment * 10 + share * 20
        entry = EntryTopic(id, new_score - old_zcore, new_score)
        if len(heap) < 5:
            heapq.heappush(heap, entry)
        else:
            heapq.heappush(heap, entry)
            heapq.heappop(heap)
    heap = sorted(heap, key=lambda x: (-x.change_score, -x.id))
    for _ in range(len(heap)):
        print(heap[_].id, heap[_].new_score)
