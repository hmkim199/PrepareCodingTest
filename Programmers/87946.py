# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도

def dfs(order, k, dungeons, count):
    global cnt
    # 모두 방문 시도 했으면 return
    if len(order) == len(dungeons):
        cnt = max(cnt, count)
        return cnt
    
    for i in range(len(dungeons)):
        if i not in order:
            if k >= dungeons[i][0]:
                dfs(order.union({i}), k - dungeons[i][1], dungeons, count+1)
            else:
                dfs(order.union({i}), k, dungeons, count)

def solution(k, dungeons):
    global cnt
    cnt = 0
    dfs(set(), k, dungeons, cnt)
    return cnt

print(solution(80, [[80, 20], [50, 40], [30, 10]])) # 3