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



# 다시 푼 풀이
# def solution(arr1, arr2):
#     answer = arr1
    
#     if len(arr1) != 0:
#         for i in range(len(arr1)):
#             for j in range(len(arr1[0])):
#                 answer[i][j] = arr1[i][j] + arr2[i][j]
    
#     return answer



# 다른 사람 풀이

# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer


# zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

# ※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.

# 잘 이해되지 않는다면 다음 예제를 살펴보자.

# >>> list(zip([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]
# >>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# >>> list(zip("abc", "def"))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]