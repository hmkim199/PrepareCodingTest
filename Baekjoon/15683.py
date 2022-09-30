# https://www.acmicpc.net/problem/15683
# 감시

# https://na982.tistory.com/95 이거 보고 함.

from copy import deepcopy


matrix = []
N, M = map(int, input().split())

for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 1번: 동, 서, 남, 북
# 2번: 동서 / 남북
# 3번: 북동 / 남동 / 북서 / 남서
# 4번: 동서남 / 동서북 / 동남북 / 서남북
# 5번: 동서남북

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 5:
            cctv.append([i, j, matrix[i][j]-1])

rot_size = [4, 2, 4, 4, 1]

def update(dir, cctv):
    dir %= 4
    if dir == 0:
        for i in range(cctv[1]+1, M):
            if matrix[cctv[0]][i] == 6: break
            matrix[cctv[0]][i] = -1
    elif dir == 1:
        for i in range(cctv[0]-1, -1, -1):
            if matrix[i][cctv[1]] == 6: break
            matrix[i][cctv[1]] = -1
    elif dir == 2:
        for i in range(cctv[1]-1, -1, -1):
            if matrix[cctv[0]][i] == 6: break
            matrix[cctv[0]][i] = -1
    elif dir == 3:
        for i in range(cctv[0]+1, N):
            if matrix[i][cctv[1]] == 6: break
            matrix[i][cctv[1]] = -1

def dfs(cctv_idx):
    global matrix
    global ret

    if cctv_idx == len(cctv):
        count = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    count += 1
        
        if ret > count:
            ret = count
        return
    
    type = cctv[cctv_idx][2]
    for dir in range(rot_size[type]):
        temp = deepcopy(matrix)
        if type == 0:
            update(dir, cctv[cctv_idx])
        elif type == 1:
            update(dir, cctv[cctv_idx])
            update(dir+2, cctv[cctv_idx])
        elif type == 2:
            update(dir, cctv[cctv_idx])
            update(dir+1, cctv[cctv_idx])
        elif type == 3:
            update(dir, cctv[cctv_idx])
            update(dir+1, cctv[cctv_idx])
            update(dir+2, cctv[cctv_idx])
        elif type == 4:
            update(dir, cctv[cctv_idx])
            update(dir+1, cctv[cctv_idx])
            update(dir+2, cctv[cctv_idx])
            update(dir+3, cctv[cctv_idx])
            
        dfs(cctv_idx + 1)
        matrix = temp

ret = 100
dfs(0)
print(ret)
