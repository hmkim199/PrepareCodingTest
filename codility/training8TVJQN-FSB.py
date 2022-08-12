# https://app.codility.com/c/run/training8TVJQN-FSB/
# OddOccurrencesInArray

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 0

    pair = {}
    for elem in A:
        if elem in pair:
            pair[elem] += 1
        else:
            pair[elem] = 1
    
    for elem in pair:
        if pair[elem] %2 != 0:
            answer = elem
            break
    
    return answer
