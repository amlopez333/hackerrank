def getValues():
    cities, amountOfStations = map(int, input().strip().split(' '))
    stations = list(map(int, input().strip().split(' ')))
    return cities, amountOfStations, stations
def createFlatland(cities, stations):
    return [1 if a in stations else 0 for a in range(cities)]
def findNearestStation(city, flatland):
    if(flatland[city] == 1):
        return 0
    d1 = searchLeft(flatland[:city])
    d2 = searchRight(flatland[city+1:])
    return min(d1,d2)
def searchLeft(flatland):
    if (len(flatland)==0):
        return 10**5+1
    distance = 0
    for i in range(len(flatland) - 1, -1, -1):
        distance += 1
        if (flatland[i] == 1):
            return distance  
    #Maybe there are none to the left    
    if (flatland[0] == 0):
        return 10**5+1
def searchRight(flatland):
    if (len(flatland)==0):
        return 10**5+1
    distance = 0
    for i in range(len(flatland)):
        distance += 1
        if(flatland[i] == 1):
            return distance
    #Maybe there are none to the right
    if (flatland[len(flatland)-1] == 0):
        return 10**5+1
def main():
    cities, amountOfStations, stations = getValues()
    flatland = createFlatland(cities, stations)
    distances = [findNearestStation(i, flatland) for i in range(cities)]
    print(max(distances))

main()
