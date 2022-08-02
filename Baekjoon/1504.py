# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

# 틀림. 처음 생각나는 가장 무식한 방법. -> 이동하는 길이 다른 노드 거칠 때 더 짧을 수 있다.
N, E = map(int, input().split())
dist = {}
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[(a, b)] = c
    dist[(b, a)] = c

v1, v2 = map(int, input().split())
d1 = dist.get((1, v1))
if not d1:
    d1 = 3000
d2 = dist.get((v1, v2))
if not d2:
    d2 = 3000
d3 = dist.get((v2, N))
if not d3:
    d3 = 3000

result = d1+d2+d3

d1 = dist.get((1, v2))
if not d1:
    d1 = 3000
d2 = dist.get((v2, v1))
if not d2:
    d2 = 3000
d3 = dist.get((v1, N))
if not d3:
    d3 = 3000

result = min(result, d1+d2+d3)
if result >= 3000:
    result = -1

print(result)