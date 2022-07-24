# https://www.acmicpc.net/problem/1043
# 거짓말

from collections import deque


N, M = map(int, input().split()) # 사람의 수, 파티의 수
t_num = list(map(int, input().split()))
t_cnt = t_num[0] # 진실을 아는 사람의 수
t_num = deque(t_num[1:]) # 진실을 아는 사람 번호

parties = []
lie_party = [True for _ in range(M)] # 거짓말 하는 파티인지
for _ in range(M):
    p_num = list(map(int, input().split()))
    p_cnt = p_num[0] # 파티 인원
    p_num = set(p_num[1:]) # 파티 참여 사람 번호
    parties.append(p_num) # 파티 정보 저장

while t_num:
    t = t_num.popleft() # 진실을 아는 사람
    for i in range(len(parties)):
        if lie_party[i] and t in parties[i]:
            lie_party[i] = False
            
            if len(parties[i]) > 1:
                parties[i].remove(t)
                for new_known in parties[i]:
                    t_num.append(new_known)

cnt = 0
for p in lie_party:
    if p:
        cnt += 1
print(cnt)
