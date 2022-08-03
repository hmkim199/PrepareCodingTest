# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 땅따먹기

# 시간초과
from collections import deque


def solution(land):
    maximum = 0
    queue = deque()
    for i in range(4):
        queue.append((land[0][i], (0, i)))

    while queue:
        total, pos = queue.popleft()
        if pos[0] < len(land)-1:            
            # 다음으로
            for i in range(4):
                if i != pos[1]:
                    queue.append((total+land[pos[0]+1][i], (pos[0]+1, i)))
        else:
            maximum = max(maximum, total)

    return maximum

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))