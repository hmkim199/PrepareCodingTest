# https://www.acmicpc.net/problem/18870
# 좌표 압축

# 시간 초과 + 잘못 생각함

# N = int(input())
# x = list(map(int, input().split()))

# cnt = {}
# compression = {}

# for i in x:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1

# distinct_x = sorted(list(set(x)))

# for i in range(len(distinct_x)):
#     compression[distinct_x[i]] = 0
#     for j in distinct_x[:i]:
#         compression[distinct_x[i]] += cnt[j]

# for i in x:
#     print(compression[i], end=" ")

# 잘못 생각함
# N = int(input())
# x = list(map(int, input().split()))

# compression = {}

# sorted_x = sorted(x)
# latest = -10e9-1
# latest_idx = -1
# for i in range(len(sorted_x)):
#     num = sorted_x[i]
#     if num != latest:
#         compression[num] = i
#         latest = num
#         latest_idx = i

# for i in range(len(x)):
#     print(compression[x[i]], end=" ")


N = int(input())
x = list(map(int, input().split()))

compression = {}

distinct_x = sorted(list(set(x)))

for i in range(len(distinct_x)):
    compression[distinct_x[i]] = i

for i in x:
    print(compression[i], end=" ")