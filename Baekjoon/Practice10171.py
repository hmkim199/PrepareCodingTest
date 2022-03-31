# https://www.acmicpc.net/problem/10171
# 고양이 

print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

# https://www.acmicpc.net/problem/10172
# 개

print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")

# https://www.acmicpc.net/problem/10809
# 알파벳 찾기

S = input()
# 97~122 소문자
for i in range(97, 123):
    c = chr(i)
    print(S.find(c), end=" ")


# https://programmers.co.kr/learn/courses/30/lessons/12926
# 시저 암호

# 예전 코드
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


# 이번 코드
def caesar(last, ascii_c, n):
    new_c = ascii_c+n
    if new_c > last:
        new_c -= 26
    return chr(new_c)

def solution(s, n):
    answer = ''
#     ord로 바꾼 후 n만큼 밀기. 소문자는 97-122, 대문자는 65-90
    for c in s:
        ascii_c = ord(c)
        if 97 <= ascii_c <= 122:
            answer += caesar(122, ascii_c, n)
        elif 65 <= ascii_c <= 90:
            answer += caesar(90, ascii_c, n)
        else:
            answer += c
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12925
# 문자열을 정수로 바꾸기

def solution(s):  
    return int(s)