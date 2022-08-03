# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 땅따먹기

# 검색해서 풂.
# 참고: https://unie2.tistory.com/1050

def solution(land):
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                for k in range(len(land[0])):
                    if j == k:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+land[i][j])
    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))