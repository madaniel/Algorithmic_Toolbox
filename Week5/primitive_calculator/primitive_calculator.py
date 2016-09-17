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

    for idx, m in enumerate(max_division_list):
        if m == 0:
            continue
        min_list = [math.inf] * 3

        # Option 1 - last number + 1
        min_list[0] = (max_division_list[idx-1] + 1)
        # Option 2 - current number / 2
        if idx % 2 == 0:
            min_list[1] = (max_division_list[idx//2] + 1)
        # Option 3 - current number / 3
        if idx % 3 == 0:
            min_list[2] = (max_division_list[idx//3] + 1)

        max_division_list[idx], min_index = min(min_list), min_list.index(min(min_list))

        # Option 1 - last number + 1
        if min_index == 0:
            operations[idx] = 1

        # Option 2 - current number / 2
        elif min_index == 1:
            operations[idx] = 2

        # Option 3 - current number / 3
        elif min_index == 2:
            operations[idx] = 3

    sequence = []
    idx = len(operations) - 1

    while idx > 1:
        current = int(operations[idx])
        sequence.append(current)

        if current != 1:
            idx = (idx // current)
        else:
            idx -= 1

    start_number = 1
    sequence.reverse()

    for i, item in enumerate(sequence):

        if item == 1:
            start_number += 1
            sequence[i] = start_number
        elif item == 2:
            start_number = start_number * 2
            sequence[i] = start_number
        elif item == 3:
            start_number = start_number *3
            sequence[i] = start_number

    sequence.insert(0, 1)

    return sequence




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
"""
input = input()
n = int(input)
sequence = list(better(n))
print (len(sequence)-1)
for x in sequence:
    print(x, end=' ')

