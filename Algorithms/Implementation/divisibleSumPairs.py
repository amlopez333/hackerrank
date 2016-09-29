def getPairs(a, k):
    pairs = [(i, j) for i in range(len(a)) for j in range(len(a))
             if(i < j and (a[i] + a[j]) % k == 0)
             ]
    return pairs
def length(pairs):
    return len(pairs)
def getValues():
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    return n, k, a

def main():
    n, k, a = getValues()
    pairs = getPairs(a, k)
    amount = length(pairs)

    print(amount)

main()
