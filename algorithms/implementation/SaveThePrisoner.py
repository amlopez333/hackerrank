def getTestCaseAmount():
    return int(input().strip())

def getValues():
    prisoners, sweets, prisonerID = map(int, input().strip().split(' '))
    return prisoners, sweets, prisonerID

def getLastLinearPos(sweets, prisonerID):
     return sweets + prisonerID - 1
    
def cycleAround(linearPosition, prisoners):
    position = linearPosition % prisoners
    if(position == 0):
        return prisoners
    return position

def main():
    t = getTestCaseAmount()
    for x in range(t):
        prisoners, sweets, prisonerID = getValues()
        lastLinearPos = getLastLinearPos(sweets, prisonerID)
        if(lastLinearPos > prisoners):
            print(cycleAround(lastLinearPos, prisoners))
        else:
            print(lastLinearPos)
main()
