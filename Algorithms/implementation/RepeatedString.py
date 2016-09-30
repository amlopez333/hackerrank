def getValues():
    s = input().strip()
    n = int(input().strip())
    return s, n
def main():
    s, n = getValues()
    if(s.count('a') == len(s)):
        print(n)
    else:
        amountA = s.count('a')
        wholes = n//len(s) * amountA
        remainder = s[:n%len(s)].count('a')
        a = wholes +remainder
        print(a)
main()
    
