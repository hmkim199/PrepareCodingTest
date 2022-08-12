# # https://school.programmers.co.kr/learn/courses/30/lessons/49994
# # 방문 길이

# def solution(dirs):
#     x = 0
#     y = 0
#     visited = set()

#     move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     for dir in dirs:
#         dx, dy = move[dir]
#         if -5 <= x+dx <= 5 and -5 <= y+dy <= 5: # 경계 확인

#             # (출발지, 도착지), (도착지, 출발지) 정보가 visited에 없으면 아직 방문하지 않은 길.
#             if ((x, y), (x+dx, y+dy)) and ((x+dx, y+dy), (x, y)) not in visited: 
#                 visited.add(((x, y), (x+dx, y+dy)))
#             x = x+dx
#             y = y+dy
#     return len(visited)


# # https://school.programmers.co.kr/learn/courses/30/lessons/49993
# # 스킬트리

# def solution(skill, skill_trees):
#     answer = 0
#     for skill_tree in skill_trees:
#         ordering = -1 # 스킬 트리의 순서 맞는지 체크하기 위한 변수
#         right = True # 올바른 스킬 트리인지 확인하는 변수
#         pre_skill_ok = True # 선행스킬을 배웠는지 확인하는 변수

#         # 정해진 스킬 순서대로 하나씩 스킬 트리에서 몇 번째 인덱스인지 확인.
#         for i in range(len(skill)):
#             idx = skill_tree.find(skill[i]) # 해당 숫자 없으면 -1 반환
#             if idx == -1:
#                 pre_skill_ok = False # 해당 스킬이 스킬 트리에 없기 때문에 선행 스킬 만족 안 함.
#             else:
#                 if not pre_skill_ok: # 선행 스킬을 모두 배우지 않으면 올바르지 않은 스킬 트리
#                     right = False
#                     break
#                 if ordering > idx: # 정해진 스킬 순서대로 인덱스 확인할 때 점점 더 인덱스가 커져야 올바른 스킬 트리.
#                     right = False
#                     break
#                 ordering = idx
#         if right:
#             answer += 1
              
#     return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 쿼드압축 후 개수 세기


def solution(arr):
    def quadtree(x, y, n, arr):
        if n == 1:
            if arr[x][y] == 0:
                return 1, 0
            else:
                return 0, 1

        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[x][y] != arr[i][j]:
                    zero = 0
                    one = 0
                    for k in range(2):
                        for l in range(2):
                            new_n = n//2
                            new_x = x + new_n * k
                            new_y = y + new_n * l
                            new_zero, new_one = quadtree(new_x, new_y, new_n, arr)
                            zero += new_zero
                            one += new_one
                    return zero, one

        if arr[x][y] == 0:
            return 1, 0
        else:
            return 0, 1

                   
    return list(quadtree(0, 0, len(arr), arr))

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # 4 9
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])) # 10 15