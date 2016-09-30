def getValues():
    n = int(input().strip())
    clouds = [int(c) for c in input().strip().split(' ')]
    return n, clouds
def move(clouds, pos):
    if (pos + 2 < len(clouds) and not clouds[pos+2]):
        return pos + 2
    return pos + 1

def main():
    n, clouds = getValues()
    pos = 0
    count = 0
    while (pos < n - 1):
        pos = move(clouds, pos)
        count += 1
    print(count)

main()
