# Uses python2
import timeit
import random
import sys
from itertools import imap
"""
def gcd(a, b):
    current_gcd = 1
    for d in xrange(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
"""

def gcd(a, b):
    gcd_num = 1

    left = max(a, b)
    right = min(a, b)

    while True:
        if left % right == 0:
            gcd_num = right
            break
        else:
            tmp = right
            right = left % right
            left = tmp

    return gcd_num

"""
def test_bad():
    print gcd(28851538, 1183019)

def test_good():
    print gcd_2(2 * 10 ** 9, random.randint(1, 2 * 10 ** 9))
"""

if __name__ == "__main__":
    #print timeit.timeit(test_bad, number=1)
    #print timeit.timeit(test_good, number=1)
    #while True:
    #    num1 = random.randint(1, 2 * 10 ** 7)
    #    num2 = random.randint(1, 2 * 10 ** 7)
    #    print num1, num2
    #    assert gcd(num1, num2) == gcd_2(num1, num2)

        #    break

    input = raw_input()
    a, b = imap(int, input.split())
    print gcd(a, b)
