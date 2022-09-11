# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]

    words_set = set([words[0]])
    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1] and words[i] not in words_set:
            words_set.add(words[i])
        else:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
    return answer