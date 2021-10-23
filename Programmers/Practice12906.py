# https://programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어


# 예전 코드
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
        #print(answer)
    return answer


# 지금 코드
def solution(arr):
    answer = []
    prev = -1
    
    for i in arr:
        if prev != i:
            answer.append(i)
        prev = i
    return answer


# 다른 사람 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a