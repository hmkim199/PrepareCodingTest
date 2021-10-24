# https://programmers.co.kr/learn/courses/30/lessons/17682
# [1차] 다트 게임

#예전 코드
def solution(dartResult):
    answer = []
    temp = int(dartResult[0])
    if dartResult[1].isdigit() == True:
        temp = int(dartResult[:2])
    for i in range(1, len(dartResult)):
        if dartResult[i].isdigit() == True:
            if dartResult[i-1].isdigit() == True:
                continue
            answer.append(temp)
            temp = 0
            if i != len(dartResult)-1 and dartResult[i+1].isdigit() == True:
                temp += int(dartResult[i:i+2])
            else:
                temp += int(dartResult[i])
        elif dartResult[i] == 'D':
            temp = temp ** 2
        elif dartResult[i] == 'T':
            temp = temp ** 3
        elif dartResult[i] == '*':
            if len(answer) == 0:
                temp *= 2
            else:
                temp *= 2
                answer[-1] *= 2
        elif dartResult[i] == '#':
            temp = 0 - temp
        print(temp)
        print(answer)
    answer.append(temp)
    return sum(answer)




# 지금 코드
def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i > 0 and dartResult[i-1].isdigit():
                answer[-1] *= 10
            else:
                answer.append(int(dartResult[i]))
        elif dartResult[i].isalpha():
            if dartResult[i] == "D":
                answer[-1] **= 2
            elif dartResult[i] == "T":
                answer[-1] **= 3
        else:
            if dartResult[i] == "*":
                answer[-1] *= 2
                if len(answer) > 1: answer[-2] *= 2 
            else:
                answer[-1] *= -1
    return sum(answer)