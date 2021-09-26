# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

def solution(s):
    answer = ''
    
    big = True
    
    for c in s:
        if c == " ":
            answer += c
            big = True
            continue
        if big:
            answer += c.upper()
            big = False
        else: 
            answer += c.lower()
            big = True
    return answer



# 다른 사람 풀이
def solution(s):

    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
