def getValues():
    n = int(input().strip())
    arr = [int(a) for a in input().strip().split(' ')]
    return n, arr
def getSet(arr):
    arr = set(arr)
    return arr
def getCount(elemInSet, arr):
    return arr.count(elemInSet)
def main():
    n, arr = getValues()
    arrToSet = getSet(arr)
    totalPairs = 0
    for elem in arrToSet:
        totalPairs += getCount(elem, arr)//2
    print(totalPairs)
main()
