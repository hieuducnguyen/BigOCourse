"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import heapq


class EntryTopic:
    def __init__(self, id, change_score, new_score):
        self.id = id
        self.change_score = change_score
        self.new_score = new_score

    def __lt__(self, other):
        if self.change_score == other.change_score:
            return self.id > other.id
        return self.change_score > other.change_score


if __name__ == '__main__':
    N = int(input())
    heap = []
    for _ in range(N):
        id, old_zcore, mention, like, comment, share = map(int, input().split())
        new_score = mention * 50 + like * 5 + comment * 10 + share * 20
        entry = EntryTopic(id, new_score - old_zcore, new_score)
        heap.append(entry)
    heapq.heapify(heap)
    for _ in range(5):
        entry = heapq.heappop(heap)
        print(entry.id, entry.new_score)
