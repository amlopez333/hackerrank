def getEarly(a):
    early = [n for n in a if n < 0]
    return early
def getOnTime(a):
    onTime = [n for n in a if n == 0]
    return onTime
def getAmount(students):
    return len(students)
def isCanceled(amount,k):
    if(amount < k):
        return True
    return False

def getTestCase():
    t = int(input().strip())
    return t
def getValues():
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    return n, k, a
def cancel(canceled):
    if(canceled):
        return "YES"
    return "NO"
def main():
    t = getTestCase()
    for i in range(t):
        n, k, a = getValues()
        early = getEarly(a)
        onTime = getOnTime(a)
        amount = getAmount(early) + getAmount(onTime)
        canceled = isCanceled(amount, k)
        print(cancel(canceled))
main()        
    
