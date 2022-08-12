# https://app.codility.com/c/run/trainingM2TKVQ-HNV/
# CyclicRotation

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6

    # 이거 없으면 틀림..
    if len(A) == 0:
        return A
    length = len(A)
    k = K % length if K > length else K
    
    return A[-k:] + A[:-k]

print(solution([1, 2, 3, 4, 5], 5))