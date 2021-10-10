"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def count_point():
    num_card = input()
    card_list = list(map(int, input().split()))
    S_score, D_score = 0, 0
    s_pointer = 0
    d_pointer = len(card_list) - 1
    player_s = True
    while s_pointer <= d_pointer:
        if player_s:
            if card_list[s_pointer] < card_list[d_pointer]:
                S_score += card_list[d_pointer]
                d_pointer -= 1
            else:
                S_score += card_list[s_pointer]
                s_pointer += 1
        else:
            if card_list[s_pointer] < card_list[d_pointer]:
                D_score += card_list[d_pointer]
                d_pointer -= 1
            else:
                D_score += card_list[s_pointer]
                s_pointer += 1
        player_s = not player_s
    print(S_score, D_score)


if __name__ == '__main__':
    count_point()
