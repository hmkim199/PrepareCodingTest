# https://www.acmicpc.net/problem/14889
# 스타트와 링크

from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

# 팀 나누기 N//2명씩
people = [i for i in range(N)]
options = list(combinations(people, N//2))
op_team1 = options[:len(options)//2]
op_team2 = options[len(options)//2:][::-1] # options의 뒤 절반을 뒤집어서 저장하면 순서에 맞게 두 팀 정보 저장 됨!

# print(team_1, team_2)

minimum = 10e9
# 능력치 합 구하기
for k in range(len(op_team1)):
    sum_team1 = 0
    sum_team2 = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            sum_team1 += S[op_team1[k][i]][op_team1[k][j]]
            sum_team1 += S[op_team1[k][j]][op_team1[k][i]]
            sum_team2 += S[op_team2[k][i]][op_team2[k][j]]
            sum_team2 += S[op_team2[k][j]][op_team2[k][i]]
    # print(team1, team2)
    minimum = min(minimum, abs(sum_team1 - sum_team2))

print(minimum)