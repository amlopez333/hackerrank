import itertools
def getT():
    t = int(input().strip())
    return t
def getW():
    w = input().strip()
    return w
def getIterator(w):
    return iter(itertools.permutations(w))
def getNext(iterator):
    return next(iterator)
def findNextBigger(w):
    iterator = getIterator(w)
    current = ()
    if(w.count(w[0])/len(w) == 1):
        return "no answer"
    try:
        while(current != None):
            current = getNext(iterator)
            if(current > tuple(w)):
                break
    except:
        return("no answer")
    try:
        while(getNext(iterator) != None):
           
            if(getNext(iterator) < current and getNext(iterator()> tuple(w))):
                
                current = getNext(iterator)
            
            
        return(''.join(current))
    except:   
        return(''.join(current))
def main():
    t = getT()
    for i in range(t):
        w = getW()
        print(findNextBigger(w))

main()
    
