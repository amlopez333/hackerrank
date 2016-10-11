def getT():
    t = int(input().strip())
    return t
def getW():
    w = list(input().strip())
    return w
def getNonIncreasingIndex(w):
    for i in range(len(w)-1, -1, -1):
        if w[i-1]<w[i]:
            return i
    return i
def getPivot(w,i):
    return i-1
def getNextAfterPivot(w, i, pivot):
    for j in range(len(w)-1, -1, -1 ):
        if(w[j]>w[pivot]):
            return j
    return indexOfNextGreatest
def swap(w, j, pivot):
    w[j], w[pivot] = w[pivot], w[j]
    return w
def reverseSuffix(w,i):
    w = w[:i] + w[len(w) - 1 : i - 1 : -1]
    return w
def buildString(w):
    return ''.join(w)
def getNextPermutation(w):
    nonIncreasingIndex = getNonIncreasingIndex(w)
    if(nonIncreasingIndex <= 0):
        return "no answer"
    pivot = getPivot(w, nonIncreasingIndex)
    nextAfterPivot = getNextAfterPivot(w, nonIncreasingIndex, pivot)
    w = swap(w, nextAfterPivot, pivot)
    w = reverseSuffix(w, nonIncreasingIndex)
    return buildString(w)
def main():
    t = getT()
    for i in range(t):
        w = getW()
        print(getNextPermutation(w))

main()
    
