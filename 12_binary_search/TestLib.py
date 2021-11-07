import bisect

if __name__ == '__main__':
    arr = [0, 2, 4, 6]
    index = bisect.bisect_left(arr, -1)
    print(index)
