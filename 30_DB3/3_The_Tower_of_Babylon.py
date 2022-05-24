"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 27/01/2022
"""


class Rock:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # if self.x < self.y:
        #     self.x, self.y = self.y, self.x
        # if self.x < self.z:
        #     self.x, self.z = self.z, self.x
        # if self.y < self.z:
        #     self.y, self.z = self.z, self.y

    def __gt__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return self.z > other.z
            else:
                return self.y > other.y
        else:
            return self.x > other.x

    def __str__(self):
        return "Rock(x={}, y={}, z={})".format(self.x, self.y, self.z)


if __name__ == '__main__':
    num_test = 1
    while True:
        num_rock = int(input())
        if num_rock == 0:
            break
        rock_list = []
        for i in range(num_rock):
            x, y, z = map(int, input().split())
            rock_1 = Rock(x, y, z)
            rock_list.append(rock_1)
            rock_2 = Rock(x, z, y)
            rock_list.append(rock_2)
            rock_3 = Rock(y, z, x)
            rock_list.append(rock_3)
            rock_4 = Rock(y, x, z)
            rock_list.append(rock_4)
            rock_5 = Rock(z, x, y)
            rock_list.append(rock_5)
            rock_6 = Rock(z, y, x)
            rock_list.append(rock_6)
        rock_list.sort(reverse=True)
        len_rock_list = len(rock_list)
        max_height_list = [0] * len_rock_list
        max_height = 0
        for i in range(len_rock_list):
            max_height_list[i] = rock_list[i].z
            max_height = max(max_height, max_height_list[i])
            for j in range(i):
                if rock_list[i].x < rock_list[j].x and rock_list[i].y < rock_list[j].y:
                    max_height_list[i] = max(max_height_list[i], max_height_list[j] + rock_list[i].z)
                    max_height = max(max_height, max_height_list[i])
        print("Case {}: maximum height = {}".format(num_test, max_height))
        num_test += 1
