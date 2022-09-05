# https://www.acmicpc.net/problem/1991
# 트리 순회

from collections import deque


class Node:
    def __init__(self):
        self.value = None
        self.left_child = None
        self.right_child = None

N = int(input())
nodes = [Node() for _ in range(N)]
for _ in range(N):
    value, left_val, right_val = input().split()
    node = nodes[ord(value)-65]
    node.value = value
    
    if left_val != ".":
        left_child = nodes[ord(left_val)-65]
        left_child.value = left_val
        node.left_child = left_child
    
    if right_val != ".":
        right_child = nodes[ord(right_val)-65]
        right_child.value = right_val
        node.right_child = right_child

def preorder(node):
    if not node:
        return ""
    return node.value + preorder(node.left_child) + preorder(node.right_child)
    
def inorder(node):
    if not node:
        return ""
    return inorder(node.left_child) + node.value + inorder(node.right_child)

def postorder(node):
    if not node:
        return ""
    return postorder(node.left_child) + postorder(node.right_child) + node.value

print(preorder(nodes[0]))
print(inorder(nodes[0]))
print(postorder(nodes[0]))