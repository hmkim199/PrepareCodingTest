# https://www.acmicpc.net/problem/2884
# 알람 시계


H, M = map(int, input().split())

total = H * 60 + M
result = total - 45

if result < 0:
    print(23, result%60)
else:
    print(result // 60, result % 60)


# ===============================================
# https://www.acmicpc.net/problem/2908
# 상수 

A, B = map(int, input().split())

A, B = int(str(A)[::-1]), int(str(B)[::-1])

print(max(A, B))

# ===============================================
# https://www.acmicpc.net/problem/2920
# 음계 

ascending = [i+1 for i in range(8)]

nums = list(map(int, input().split()))

if nums == ascending:
    print("ascending")
elif nums == ascending[::-1]:
    print("descending")
else:
    print("mixed")

# ===============================================
# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int, str(n)))[::-1]
    return answer

# ===============================================
# https://programmers.co.kr/learn/courses/30/lessons/12931
# 자릿수 더하기

def solution(n):
    answer = sum(list(map(int, str(n))))

    return answer