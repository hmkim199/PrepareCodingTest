# https://www.acmicpc.net/problem/1931
# 회의실 배정

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

schedule = []
schedule.append(meetings[0])
for i in range(1, N):
    if meetings[i][0] >= schedule[-1][1]:
        schedule.append(meetings[i])
    
print(len(schedule))

