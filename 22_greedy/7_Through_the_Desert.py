"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/01/2022
"""

FUEL = "Fuel consumption"
GOAL = "Goal"
MECHANIC = "Mechanic"
LEAK = "Leak"
GAS = "Gas station"


def cal_energy(distance, num_leak, consume_energy):
    return distance / 100 * consume_energy + num_leak * distance


if __name__ == '__main__':
    last_point, num_leak, consume_energy, energy_total, tmp_contain = 0, 0, 0, 0, 0
    while True:
        input_text = input()
        if input_text == "0 Fuel consumption 0":
            break
        if input_text.__contains__(GOAL):
            point = int(input_text.split(GOAL)[0])
            cost = cal_energy(point - last_point, num_leak, consume_energy)
            energy_total += cost
            tmp_contain = max(tmp_contain, energy_total)
            print("{:.3f}".format(tmp_contain))
            last_point, num_leak, consume_energy, energy_total, tmp_contain = 0, 0, 0, 0, 0
            continue
        if input_text.__contains__(FUEL):
            point, new_consum_energy = map(int, input_text.split(FUEL))
            cost = cal_energy(point - last_point, num_leak, consume_energy)
            energy_total += cost
            consume_energy = new_consum_energy
        elif input_text.__contains__(LEAK):
            point = int(input_text.split(LEAK)[0])
            cost = cal_energy(point - last_point, num_leak, consume_energy)
            energy_total += cost
            num_leak += 1
        elif input_text.__contains__(GAS):
            point = int(input_text.split(GAS)[0])
            cost = cal_energy(point - last_point, num_leak, consume_energy)
            energy_total += cost
            tmp_contain = max(tmp_contain, energy_total)
            energy_total = 0
        else:
            point = int(input_text.split(MECHANIC)[0])
            cost = cal_energy(point - last_point, num_leak, consume_energy)
            energy_total += cost
            num_leak = 0
        last_point = point
