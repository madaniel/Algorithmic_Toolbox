# Uses python3

import math
"""
def better(price):
    coins_list = [1, 5, 6]
    money_list = [math.inf] * (price + 1)
    money_list[0] = 0

    for c in coins_list:
        for idx, m in enumerate(money_list):
            if idx >= c:
                money_list[idx] = min(money_list[idx], (money_list[idx-c] + 1))

    return money_list
"""


def better(number):
    max_division_list = [math.inf] * (number + 1)
    max_division_list[0] = 0
    max_division_list[1] = 0

    operations = [""] * (number + 1)

    for dev in max_division_list:
        for idx, m in enumerate(max_division_list):
            if m == 0:
                continue
            min_list = []

            # Option 1 - last number + 1
            min_list.append(max_division_list[idx-1] + 1)
            # Option 2 - current number / 2
            if idx % 2 == 0:
                min_list.append(max_division_list[idx//2] + 1)
            # Option 3 - current number / 3
            if idx % 3 == 0:
                min_list.append(max_division_list[idx//3] + 1)

            max_division_list[idx], min_index = min(min_list), min_list.index(min(min_list))

            # Option 1 - last number + 1
            if min_index == 0:
                operations[idx] = str(operations[idx]) + "+1"

            # Option 2 - current number / 2
            elif min_index == 1:
                operations[idx] = str(operations[idx]) + "*2"

            # Option 3 - current number / 3
            elif min_index == 2:
                operations[idx] = str(operations[idx]) + "*3"

    #print (operations)
    return max_division_list


print (better(15))
"""

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = input()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

"""