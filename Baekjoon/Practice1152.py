# https://www.acmicpc.net/problem/1152
# 단어의 개수

print(len(input().split()))


#===========================================
# https://www.acmicpc.net/problem/1157
# 단어 공부

word = list(input().lower())
word_set = set(word)
count = 0
mode = ""
duplicate = False
for s in word_set:
    cnt = word.count(s)
    if count < cnt:
        duplicate = False
        count = cnt
        mode = s
    elif count == cnt:
        duplicate = True

if duplicate:
    print("?")
else:
    print(mode.upper())


# ==========================================
# https://www.acmicpc.net/problem/1330
# 두 수 비교하기

A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


# =============================================================
# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

def solution(arr1, arr2):
    answer = arr1
    
    if len(arr1) != 0:
        for i in range(len(arr1)):
            for j in range(len(arr1[0])):
                answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer


# =============================================================
# https://programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 가리기

def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    print(answer)
    return answer