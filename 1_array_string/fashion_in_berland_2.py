if __name__ == '__main__':
    print("YES" if min(1, int(input()) - 1) == input().split().count("0") else "NO")
