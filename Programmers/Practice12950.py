# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

def solution(arr1, arr2):
    answer = [[]]
    row = len(arr1)
    col = len(arr1[0])
    answer = arr1
    
    for i in range(row):
        for j in range(col):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer