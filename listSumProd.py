
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

# get numbers 
inputStr = input("enter number separted by spaced end with enter: ")
splitInput = inputStr.split()
intList = []

# cast to ints
for s in splitInput:
    try:
        num = int(s) 
        intList.append(num)  
    except ValueError:
        print(f"Cannot convert '{s}' to an integer. Skipping...")

# call functions
sumOfList = sumList(intList)
productOfList = multiplyList(intList)

# print
print("sum", sumOfList)
print("product", productOfList)

