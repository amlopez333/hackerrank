def getValues():
    n, k = [int(a) for a in input().strip().split(' ')]
    numberSet = [int(a) for a in input().strip().split(' ')]
    return n,k , numberSet
def getSubSet(numberSet,k):
    subset = [0] * k
    for number in numberSet:
        subset[number % k] += 1
    return subset
def getLength(subset, k):
    length = 0
    for a in range(1, (k + 1)//2):
        length += max(subset[a], subset[k-a])
    if k % 2 == 0 and subset[k // 2]:
        length += 1
    if subset[0]:
        length += 1
    return length

def main():
    n, k, numberSet = getValues()
    k = int(k)
    subset = getSubSet(numberSet, k)
    n = getLength(subset, k)
    print(n)
    
main()
