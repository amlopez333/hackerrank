def getValues():
    n = int(input().strip())
    sticks = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    return n, sticks
def cut(stickLength, sticks):
    sticks = [stick - stickLength for stick in sticks
              if (stick - stickLength > 0)]
    return sticks
def getMinStickLength(sticks):
    #could be sorted ascending, then return sticks[1]
    #could be linear search
    return min(sticks)
def getLength(sticks):
    return len(sticks)
def main():
    n, sticks = getValues()
    while(getLength(sticks)):
        print(getLength(sticks))
        stickLength = getMinStickLength(sticks)
        sticks = cut(stickLength, sticks)

main()
    
