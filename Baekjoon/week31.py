# # https://school.programmers.co.kr/learn/courses/30/lessons/84512
# # 모음 사전

# from itertools import product

# def solution(word):
#     alphabet = ['A', 'E', 'I', 'O', 'U']
#     dictionary = []
#     for i in range(1, 6):
#         dictionary += product(alphabet, repeat=i) # product는 중복 순열. alphabet의 요소들 중에서 반복해서 i개 뽑아 줄세워서 리턴.
    
#     dictionary.sort()
#     return dictionary.index(tuple(word))+1


# # https://school.programmers.co.kr/learn/courses/30/lessons/86971
# # 전력망을 둘로 나누기

# from collections import deque

# def bfs(tree, start):
#     visited = [False for _ in range(len(tree))]
#     visited[start] = visited[0] = True
#     q = deque()
#     q.append(start)
    
#     while q:
#         node = q.popleft()
#         for adj_node in tree[node]:
#             if not visited[adj_node]:
#                 visited[adj_node] = True
#                 q.append(adj_node)
    
#     answer = 0
#     for is_visited in visited[1:]:
#         if is_visited:
#             answer += 1
#     return answer

# def solution(n, wires):
#     answer = n
#     tree = [set() for _ in range(n+1)]
#     for a, b in wires:
#         tree[a].add(b)
#         tree[b].add(a)
    
#     for a, b in wires:
#         tree[a].remove(b)
#         tree[b].remove(a)
        
#         network1 = bfs(tree, a)
#         network2 = n - bfs(tree, a)
#         print(abs(network1 - network2))
#         answer = min(answer, abs(network1 - network2))
        
#         tree[a].add(b)
#         tree[b].add(a)
    
#     return answer

# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3


# https://school.programmers.co.kr/learn/courses/30/lessons/87377
# 교점에 별 만들기

# x, y가 너무 헷갈려서 머리 터지는줄.

def solution(line):
    coordinate = []
    answer = []
    for i in range(len(line)):
        for j in range(i, len(line)):
            a, b, e = line[i][0], line[i][1], line[i][2]
            c, d, f = line[j][0], line[j][1], line[j][2]
            
            if a*d - b*c == 0:
                continue
            
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            if x == int(x) and y == int(y):
                coordinate.append([int(x), int(y)])
    
    min_x, max_x = min(coordinate, key = lambda x: x[0])[0], max(coordinate, key = lambda x: x[0])[0]
    min_y, max_y = min(coordinate, key = lambda x: x[1])[1], max(coordinate, key = lambda x: x[1])[1]
    
    answer = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for x, y in coordinate:
        dx = abs(x-min_x)
        dy = abs(y-max_y)
        answer[dy][dx] = "*"

    for i in range(len(answer)):
        answer[i] = "".join(answer[i])

    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))