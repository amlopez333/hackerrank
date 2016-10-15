def getValues():
    chapters, maxProblemAmount = map(int, input().strip().split(' '))
    problemsPerChapter = list(map(int, input().strip().split(' ')))
    return chapters, maxProblemAmount, problemsPerChapter
def main():
    chapters, maxProblemAmount, problemsPerChapter = getValues()
    page = 1
    totalSpecial = 0
    for i in range(chapters):
        problems = problemsPerChapter[i]
        problemIndex = 1
        specialPerChapter = 0
        problemCount = 0
        while(problemIndex <= problems):
            if(problemCount == maxProblemAmount):
                page += 1
                problemCount = 0
            if(problemIndex == page):
                specialPerChapter += 1
            problemIndex += 1
            problemCount += 1
        page += 1    
        totalSpecial+=specialPerChapter
    print(totalSpecial)
main()
