import sys
personNum = int(sys.stdin.readline())
timeList = []

timeList = list(map(int, sys.stdin.readline().split()))
timeList.sort()
allTime, addTime = 0, 0

for time in timeList:
    addTime += time
    allTime += addTime
print(allTime)