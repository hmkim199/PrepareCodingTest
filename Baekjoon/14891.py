# https://www.acmicpc.net/problem/14891
# 톱니바퀴

from collections import deque

wheels = []
for _ in range(4):
    wheels.append(list(map(int, list(input()))))

K = int(input())
for _ in range(K):
    wheel, dir = map(int, input().split())
    wheel -= 1
    q = deque([[wheel, dir]]) # 연쇄적으로 돌아가는 톱니 확인 위한 큐
    rot = set([(wheel, dir)]) # 총 어떤 톱니를 어떤 방향으로 회전해야 하는지 저장하는 집합 

    while q:
        w, d = q.popleft()
        # 톱니 1번 제외한 경우, 왼쪽 톱니 확인
        if w >= 1 and (w-1, -d) not in rot:
            if wheels[w-1][2] != wheels[w][6]:
                rot.add((w-1, -d))
                q.append([w-1, -d])
        
        # 톱니 4번 제외한 경우, 오른쪽 톱니 확인
        if w <= 2 and (w+1, -d) not in rot:
            if wheels[w+1][6] != wheels[w][2]:
                rot.add((w+1, -d))
                q.append([w+1, -d])
    
    for w, d in rot:
        if d == -1:
            wheels[w] = wheels[w][1:] + wheels[w][:1]
        else:
            wheels[w] = wheels[w][7:] + wheels[w][:7]

score = 0
for i in range(4):
    score += wheels[i][0] * 2**i

print(score)
