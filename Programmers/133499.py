# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 옹알이 (2)

def solution(babbling):
    answer = 0
    baby_word = {"aya", "ye", "woo", "ma"}
    for word in babbling:
        start = 0
        before = ""
        for i in range(1, len(word)+1):
            if word[start:i] != before and word[start:i] in baby_word:
                before = word[start:i]
                start = i
        if start == len(word):
            answer += 1
    return answer