# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

# 예전 풀이
def solution(s, n):
    answer = ''
    temp = 90
    big = False
    # 65~90, 97~122
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        big = s[i].isupper()
        temp = ord(s[i]) + n
        if big == False:
            if temp >= 123:
                temp = temp - 26
        if big == True:
            if temp >= 91:
                temp = temp - 26
        answer += chr(temp)
                
    return answer


# 지금 풀이
def solution(s, n):
    answer = ''
    big = [chr(i) for i in range(65, 91)]
    small = [chr(i) for i in range(97, 123)]
    
    for c in s:
        print(c)
        if c == " ":
            answer += " "
        elif c.isupper():
            answer += big[(big.index(c) + n) % 26]
        else:
            answer += small[(small.index(c) + n) % 26]
    return answer