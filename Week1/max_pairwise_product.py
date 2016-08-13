# Uses python2
import random

n = int(raw_input())
a = [int(x) for x in raw_input().split()]
assert(len(a) == n)


"""
def func_1():
    result = 0
    for i in xrange(0, n):
        for j in xrange(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result
"""

def func_2():
    max_idx_a = -1
    max_idx_b = -1

    # Finding the 1st largest number
    for i in xrange(n):
        if max_idx_a == -1 or a[i] > a[max_idx_a]:
            max_idx_a = i

    for j in xrange(n):
        if j != max_idx_a and max_idx_b == -1 or a[j] > a[max_idx_b] and j != max_idx_a:
            max_idx_b = j

    #print max_idx_a
    #print max_idx_b

    return a[max_idx_a] * a[max_idx_b]

print func_2()


"""

while True:


    n = random.randint(2, 10 ** 4)
    a = [random.randint(2, 10 ** 5) for x in xrange(n)]

    result_1 = func_1()
    result_2 = func_2()


    if result_1 != result_2:
        print a
        print result_1
        print result_2
        break

    count += 1
    print count
"""
