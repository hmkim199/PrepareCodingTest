# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 위장

# 아이디어: (카테고리별 개수 + 안 입는 경우의 수 1개) 를 카테고리마다 곱해서 -1(아무것도 안 입는 경우의 수) 해주기.

def solution(clothes):
    answer = 1
    closet = {}
    for cloth, category in clothes:
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
    
    for key in closet:
        answer *= (closet[key]+1)
    return answer-1