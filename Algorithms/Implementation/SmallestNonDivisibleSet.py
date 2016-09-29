import itertools
def createSubsets(numberSet, r):
    return itertools.combinations(numberSet, r)

def getSubsets(iterSubset):
    subsets = [sub for sub in iterSubset]
    return subsets
def getValues():
    n, k = [int(a) for a in input().strip().split(' ')]
    numberSet = [int(a) for a in input().strip().split(' ')]
    return n,k , numberSet
def isSetDivisible(subset, k):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            
            if((subset[i]+subset[j]) % k == 0):
                return True
    return False
def findSet(n, numberSet, k):
    found = False
    while(n > 0 and not found):    
        iterSubset = createSubsets(numberSet, n)
        subsets = getSubsets(iterSubset)
        divisibles = {}
        for sub in subsets:
            divisibles[sub] = isSetDivisible(sub, k)
        for key in divisibles:
            if not (divisibles[key]):
                return n
        n-=1
    return n

def main():
    n, k, numberSet = getValues()
    n = findSet(n, numberSet, k)
    print(n)
    
main()
