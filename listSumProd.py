def sumList(l) -> int:
    sum = 0
    for ele in l:
        sum += ele
    return sum


def multiplyList(l) -> int:
    if (len(l) == 0):
        return 0
    product = 1
    for ele in l:
        product  *= ele
    return product 