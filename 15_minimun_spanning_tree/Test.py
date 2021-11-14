import random

if __name__ == '__main__':
    V = 750
    print(V)
    for i in range(V):
        x = random.randint(-10000, 10000)
        y = random.randint(-10000, 10000)
        print(x, y)
    M = 1
    print(M)
    list_edge = []
    for i in range(M):
        x = y = 2
        while (x, y) in list_edge or x == y:
            x = random.randint(1, V)
            y = random.randint(1, V)
        list_edge.append((x, y))
        print(x, y)
