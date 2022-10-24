# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)-1, -1, -1):
        if citations[i] >= i+1:
            answer = i+1
            break
    return answer