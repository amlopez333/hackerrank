x1, v1, x2, v2 = 0,0,0,0
def isReacheable(x1,v1,x2,v2):
    if(x1 == x2):
        return True
    if(v1 > v2):
        newX1 = x1
        newX2 = x2
        while(newX1 < newX2):
            newX1 = jump(newX1, v1)
            newX2 = jump(newX2, v2)
        
        if(newX1 == newX2):
            return True
    return False

def jump(x, v):
    return x + v

def reach(x1, v1, x2, v2):
    if(isReacheable(x1,v1,x2,v2)):
        return "YES"
    return "NO"

def getValues():
    x1,v1,x2,v2 = input().strip().split(' ')
    
    x1,v1,x2,v2 = [int(x1), int(v1), int(x2), int(v2)]
    return x1,v1,x2,v2

def main():
    x1, v1, x2, v2 = getValues()
    print(reach(x1,v1,x2,v2))

main()
