import sys
N = int(sys.stdin.readline())
mitting = []
for i in range(N):
    start, fin = map(int, sys.stdin.readline().split())
    mitting.append([start, int(fin)])

mittingSort = sorted(mitting,key=lambda l:l[0])
mittingSorted = sorted(mittingSort,key=lambda l:l[1])
time = 0
last = mittingSorted[-1][1]
cnt = 0

# 알고리즘
for i in mittingSorted:
    if i[0]>=time:
        time = i[1]
        cnt+=1
print(cnt)