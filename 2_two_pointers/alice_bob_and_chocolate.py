"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def eat_chocolate():
    num_chocolate = int(input())
    chocolate = list(map(int, input().split()))
    alice = 0
    bob = len(chocolate) - 1
    alice_move, bob_move = False, False
    while alice < bob:
        if chocolate[alice] < chocolate[bob]:
            chocolate[bob] -= chocolate[alice]
            alice += 1
            alice_move = True
            bob_move = False
        elif chocolate[alice] > chocolate[bob]:
            chocolate[alice] -= chocolate[bob]
            bob -= 1
            alice_move = False
            bob_move = True
        else:
            alice += 1
            bob -= 1
            alice_move = True
            bob_move = True
    if alice_move and bob_move:
        if alice == bob:
            print(alice + 1, num_chocolate - (alice + 1))
        else:
            print(alice, num_chocolate - alice)
    elif alice_move:
        print(alice, num_chocolate - alice)
    else:
        print(alice + 1, num_chocolate - (alice + 1))


if __name__ == '__main__':
    eat_chocolate()
