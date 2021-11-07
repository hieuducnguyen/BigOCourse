"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    name_1 = input()
    name_2 = input()
    frequence_name_1 = [0 for i in range(60)]
    frequence_name_2 = [0 for i in range(60)]
    for character in name_1:
        frequence_name_1[ord(character) - ord("A")] += 1
    for character in name_2:
        frequence_name_2[ord(character) - ord("A")] += 1
    count_yes = 0
    for i in range(60):
        if frequence_name_1[i] > 0 and frequence_name_2[i] > 0:
            min_fre = min(frequence_name_1[i], frequence_name_2[i])
            count_yes += min_fre
            frequence_name_1[i] -= min_fre
            frequence_name_2[i] -= min_fre
    count_no = 0
    for i in range(60):
        if frequence_name_1[i] > 0:
            next_index = i
            if i <= ord('Z') - ord('A'):
                next_index += 32
            else:
                next_index -= 32
            if frequence_name_2[next_index] > 0:
                min_fre = min(frequence_name_1[i], frequence_name_2[next_index])
                count_no += min_fre
                frequence_name_1[i] -= min_fre
                frequence_name_2[i] -= min_fre
    print(count_yes, count_no)
