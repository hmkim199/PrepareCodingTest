# https://www.acmicpc.net/problem/1043
# 거짓말

N, M = map(int, input().split()) # 사람의 수, 파티의 수
t_num = list(map(int, input().split()))
t_cnt = t_num[0] # 진실을 아는 사람의 수
t_num = set(t_num[1:])


cnt = 0
for _ in range(M):
    p_num = list(map(int, input().split()))
    p_cnt = p_num[0]
    p_num = set(p_num[1:])

    can_lie = True
    for t in t_num:
        if t in p_num:
            print(p_num)
            can_lie = False
            break
    if can_lie:
        cnt += 1

print(cnt)
