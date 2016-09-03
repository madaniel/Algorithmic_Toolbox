# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':

    seq = input()
    a = (list(map(int, seq.split())))
    nums = input()
    b = (list(map(int, nums.split())))
    #n = data[0]
    #m = data[n + 1]
    #a = data[1: n + 1]
    #for x in data[n + 2:]:

    for x in b:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end=' ')
