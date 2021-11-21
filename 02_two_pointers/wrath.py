"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def num_survival():
    input()
    guilty = list(map(int, input().split()))
    start_pointer = len(guilty) - 1
    die_people = 0
    bell_ring = 0
    while start_pointer >= 0:
        bell_ring -= 1
        if bell_ring > 0:
            die_people += 1
        bell_ring = max(guilty[start_pointer] + 1, bell_ring)
        start_pointer -= 1
    return len(guilty) - die_people


if __name__ == '__main__':
    print(num_survival())
