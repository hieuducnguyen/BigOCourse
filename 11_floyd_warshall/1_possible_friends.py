"""
Link: https://www.spoj.com/problems/SOCIALNE/#:~:text=Two%20persons%20are%20possible%20friends,help%20him%20in%20this%20task.
Time complexity: O(V ^ 3) V: num friend
Space complexity: O(V ^ 2)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def count_possible_friend(friend_list):
    num_friend = len(friend_list)
    possible_friend = [[0] * num_friend for _ in range(num_friend)]
    for k in range(num_friend):
        for i in range(num_friend):
            for j in range(i + 1, num_friend):
                if friend_list[i][j] == "N" and friend_list[i][k] == "Y" and friend_list[k][j] == "Y":
                    possible_friend[i][j] = 1
                    possible_friend[j][i] = 1
    return possible_friend


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        friend_list = []
        first_person = list(input())
        friend_list.append(first_person)
        for i in range(1, len(first_person)):
            friend_list.append(list(input()))
        possible_friend_list = count_possible_friend(friend_list)
        max_friend_id = 0
        max_possible_friend = 0
        for i in range(len(possible_friend_list)):
            if max_possible_friend < sum(possible_friend_list[i]):
                max_friend_id = i
                max_possible_friend = sum(possible_friend_list[i])
        print("{} {}".format(max_friend_id, max_possible_friend))
