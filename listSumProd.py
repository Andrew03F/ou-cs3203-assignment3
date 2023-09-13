
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

def reverseList(l):
    return l[::-1]

def main():
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
    reversedList = reverseList(intList)

    # print
    print("sum:", sumOfList)
    print("product: ", productOfList)
    print ("reverse: ", reversedList)

if __name__ == "__main__":
    main()

# change for part10 branch 
