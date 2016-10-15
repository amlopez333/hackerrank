def getValues():
    n, jumpDistance = map(int, input().strip().split(' '))
    clouds = list(map(int, input().strip().split(' ')))
    return n, jumpDistance, clouds
def jump(cloudIndex, jumpDistance, n):
    return (cloudIndex + jumpDistance) % n
def spendEnergy(energy, cloud):
    if(cloud):
        return energy - 3
    return energy - 1
def main():
    n, jumpDistance, clouds = getValues()
    cloudIndex = 0
    energy = 100
    returned = False
    while not(returned):
        cloudIndex = jump(cloudIndex, jumpDistance, n)
        energy = spendEnergy(energy, clouds[cloudIndex])
        if not cloudIndex:
            returned = True
    print(energy)
    
    
main()
