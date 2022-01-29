# https://www.acmicpc.net/problem/1152
# 단어의 개수

# print(len(input().split()))


#===========================================
# https://www.acmicpc.net/problem/1157
# 단어 공부

# word = list(input().lower())
# word_set = set(word)
# count = 0
# mode = ""
# duplicate = False
# for s in word_set:
#     cnt = word.count(s)
#     if count < cnt:
#         duplicate = False
#         count = cnt
#         mode = s
#     elif count == cnt:
#         duplicate = True

# if duplicate:
#     print("?")
# else:
#     print(mode.upper())


# ==========================================
# https://www.acmicpc.net/problem/1330
# 두 수 비교하기

# A, B = map(int, input().split())
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")