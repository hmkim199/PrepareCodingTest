# https://www.acmicpc.net/problem/1436
# 영화감독 숌

# N = int(input())
# end_num = "666"
# end_num_len = 3
# cipher = 4
# title_num = 666
# title_cnt = 1

# while title_cnt < N:    
#     temp_cnt = title_cnt + 9**(cipher-end_num_len)*(cipher-end_num_len+1) - 9*(cipher-end_num_len) + 1
#     if temp_cnt > N:
#         start = int("1"+"0"*(cipher-end_num_len-1)+end_num)
#         end = int("9"*cipher)
#         for i in range(start, end+1):
#             if title_cnt == N: break
#             if end_num in str(i):
#                 title_num = i
#                 title_cnt += 1
#     else:
#         title_cnt = temp_cnt
#         title_num = int("9"*(cipher-end_num_len)+"666")
#     cipher += 1

# print(title_num)

N = int(input())

titles = []
title_num = 666

while True:
    if len(titles) == N: break
    if str(666) in str(title_num):
        titles.append(title_num)
    title_num += 1 

print(titles[-1])