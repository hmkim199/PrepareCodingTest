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


# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기

from collections import deque

def bfs(tree, start):
    visited = [False for _ in range(len(tree))]
    visited[start] = visited[0] = True
    q = deque()
    q.append(start)
    
    while q:
        node = q.popleft()
        for adj_node in tree[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)
    
    answer = 0
    for is_visited in visited[1:]:
        if is_visited:
            answer += 1
    return answer

def solution(n, wires):
    answer = n
    tree = [set() for _ in range(n+1)]
    for a, b in wires:
        tree[a].add(b)
        tree[b].add(a)
    
    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        
        network1 = bfs(tree, a)
        network2 = n - bfs(tree, a)
        print(abs(network1 - network2))
        answer = min(answer, abs(network1 - network2))
        
        tree[a].add(b)
        tree[b].add(a)
    
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3