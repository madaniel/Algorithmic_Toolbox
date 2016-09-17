# Uses python3


def optimal_weight(W, w):
    # write your code here




    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result






if __name__ == '__main__':
    input1 = input()
    input2 = input()
    input = "".join([input1, " ", input2])

    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
