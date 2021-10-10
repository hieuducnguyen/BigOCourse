"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

if __name__ == '__main__':
    total_tower = map(int, input())
    woods = list(map(int, input().split()))
    frequency_wood = {}
    max_frequency = 0
    for wood in woods:
        frequency_wood[wood] = frequency_wood.get(wood, 0) + 1
        max_frequency = max(max_frequency, frequency_wood[wood])
    print(max_frequency, len(frequency_wood))
