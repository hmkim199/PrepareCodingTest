# # https://school.programmers.co.kr/learn/courses/30/lessons/12924
# # 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            
            
    return answer


# # https://school.programmers.co.kr/learn/courses/30/lessons/12923
# # 숫자 블록

# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     for i in range(end//2, 0, -1):
#         for j in range(i*2, end+1, i):
#             if j-begin >= 0 and answer[j-begin] == 0:
#                 answer[j-begin] = i
#     return answer


# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10000000 if end//2 > 10000000 else end//2
#     for i in range(end//2, 0, -1):
#         for j in range(i*2, end+1, i):
#             if j-begin >= 0 and answer[j-begin] == 0:
#                 answer[j-begin] = i
#     return answer

# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10000000 if end//2 > 10000000 else end//2
#     for i in range(end_block, 0, -1):
#         for j in range(end, begin-1, -1):
#             if j < i*2:
#                 break
#             if j % i == 0:
#                 if answer[j-begin] == 0:
#                     answer[j-begin] = i

#     return answer

# # 실패
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10**7 if end//2 > 10**7 else end//2
#     for i in range(end_block, 0, -1):
#         for j in range(end//i * i, begin-1, -i):
#             if j < i*2:
#                 break
#             if j % i == 0:
#                 if answer[j-begin] == 0:
#                     answer[j-begin] = i

#     return answer

# # 남의 풀이
# import math
# def solution(begin, end):
#     result = []
#     for i in range(begin, end+1):
#         # 1은 문제 조건상 0이므로, 0을 넣어준다.
#         if i < 2:
#             result.append(0)
#             continue
#         # 소수 판별하기.
#         for j in range(2, int(math.sqrt(i))+1):
#             # 소수가 아니면, 나눈 몫을 넣어준다
#             if i % j == 0 and i // j < 10**7:
#                 result.append(i // j)
#                 break
#         else:
#             result.append(1)
        
#     return result

# # 남의 풀이 보고 푼 내풀이
def solution(begin, end):
    answer = []
    end_block = 10**7
    for i in range(begin, end+1):
        if i < 2:
            answer.append(0)
            continue
        temp = 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= end_block:
                temp = i//j
                break
        answer.append(temp)
        
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기

def convert(n, k):
    if k == 10:
        return str(n)
    d = n
    ans = ''
    while d > 0:
        ans = str(d%k) + ans
        d //= k
    return ans

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = convert(n, k)
    for i in range(len(k_num)):
        for j in range(i, len(k_num)):
            if '0' not in k_num[i:j+1] and is_prime(int(k_num[i:j+1])):
                
                if i > 0 and j < len(k_num)-2:
                    if k_num[i-1] == '0' and k_num[j+1] == '0':
                        answer += 1
                if i == 0 and j < len(k_num)-2:
                    if k_num[j+1] == '0':
                        answer += 1
                if i > 0 and j == len(k_num)-1:
                    if k_num[i-1] == '0':
                        answer += 1
                if i == 0 and j == len(k_num)-1:
                    answer += 1
    return answer

print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2

# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 멀리 뛰기

# 몇개 런타임 에러인데 아마 그냥 시간 초과인 듯.
# def jump(n, memo):
#     if n in memo:
#         return memo[n]
#     memo[n] = jump(n-1, memo) + jump(n-2, memo)
#     return memo[n]

# def solution(n):
#     memo = {1: 1, 2: 2}

#     return jump(n, memo) % 1234567

# print(solution(4))

# 풀이
def solution(n):
    jump = [0 for _ in range(2001)]
    jump[1] = 1
    jump[2] = 2
    for i in range(3, len(jump)):
        jump[i] = jump[i-2] + jump[i-1]

    return jump[n] % 1234567

print(solution(4))