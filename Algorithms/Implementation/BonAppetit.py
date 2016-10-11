def getValues():
    n, k = map(int, input().strip().split())
    costs = [int(a) for a in input().strip().split(' ')]
    charged = int(input().strip())
    return n, k, costs, charged
def getTrueCharge(costs,k):
    newCosts = costs[:k] + costs[k+1:]
    return sum(newCosts)//2
def getDifference(charged, trueCharge):
    return charged-trueCharge
def main():
    n,k,costs,charged = getValues()
    trueCharge = getTrueCharge(costs, k)
    difference = getDifference(charged, trueCharge)
    if not difference:
        print("Bon Appetit")
    else:
        print(difference)

main()
