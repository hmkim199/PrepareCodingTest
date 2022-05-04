# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

from collections import deque

class UserNode:
    """백준 유저 노드"""
    def __init__(self, user_id):
        self.user_id = user_id
        self.adjacent_users = []
        self.visited = False
    
    def add_connection(self, user):
        self.adjacent_users.append(user)

  
def bfs(graph, start_node):
    queue = deque()
    
    for user_node in graph.values():
        user_node.visited = False
    
    start_node.visited = True
    queue.append(start_node)

    while queue:
        current_user = queue.popleft()
        for neighbor in current_user.adjacent_users:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)