import sys


def max_timecount(length, antLocation):
    antLocation.sort()
    if length - antLocation[0] > -(antLocation[-1] - length):
        return length - antLocation[0]
    else:
        return -(antLocation[-1] - length)


def min_timecount(length, antLocation):
    antLocation.sort()
    for i in antLocation:
        if i > int(length / 2):
            index = antLocation.index(i)
            break
    if abs(antLocation[index] - int(length / 2)) < abs(antLocation[index - 1] - int(length / 2)):

        if antLocation[index] - int(length / 2) >= 0:
            return (length - antLocation[index])
        else:
            return (antLocation[index])
    else:
        if antLocation[index - 1] - int(length / 2) >= 0:
            return (length - antLocation[index - 1])
        else:
            return (antLocation[index])

testCase = int(sys.stdin.readline())

antLocationList = []
langthList = []

for case in range(testCase):
    antLocationList.append([])
    length, num = map(int, sys.stdin.readline().split())
    langthList.append(length)
    for ant in range(num):
        antLocationList[case].append(int(sys.stdin.readline()))

for case in range(testCase):
    print(min_timecount(langthList[case], antLocationList[case]), max_timecount(langthList[case], antLocationList[case]))
