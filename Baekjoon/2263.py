# https://www.acmicpc.net/problem/2263
# 트리의 순회

class Node:
    value = None
    left = None
    right = None

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index = [None for _ in range(n+1)]
for i in range(n):
    index[inorder[i]] = i

def get_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root_index = index[postorder[post_end]]
    left_size = root_index - in_start
    right_size = in_end - root_index
    print(inorder[root_index], end=" ")

    get_preorder(in_start, root_index - 1, post_start, post_start + left_size - 1)
    get_preorder(root_index + 1, in_end, post_start + left_size, post_end - 1)
    
get_preorder(0, len(inorder)-1, 0, len(postorder)-1)