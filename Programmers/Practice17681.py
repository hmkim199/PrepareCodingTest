# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀 지도


# 예전 코드
def solution(n, arr1, arr2):
    answer = []    
    for i in range(len(arr1)):
        temp = ''
        for num in bin(arr1[i] | arr2[i])[2:].zfill(n): # zfill(n)은 n자리가 될 때까지 빈 앞자리를 0으로 채워줌.
            if num == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer


# 현재 코드
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        originNum = bin(arr1[i] | arr2[i])[2:]
        originNum = '0' * (n-len(originNum)) + originNum
        mark = ''
        for j in originNum:
            if j == '1':
                mark += "#"
            else:
                mark += " "
        answer.append(mark)
    return answer