# 청소X -> 현재 칸 청소
# 주변 4칸 중 청소되지 않은 칸이 없으면 후진 + 1번으로 돌아감
# 주변 4칸 중 칸이 있으면 반시계 90도 회전
# 정면에 있으면 그냥 전진
def dfs(i, j, d):
    global cnt
    if arr[i][j] == 0:
        arr[i][j] = 2
        cnt += 1
    dy = d
    for _ in range(4):
        dy = (dy+3)%4
        ni, nj = i+di[dy], j+dj[dy]
        if arr[ni][nj] == 0:
            dfs(ni, nj, dy)
            return
    # 주변에 청소할 곳이 없으면
    bi, bj = i-di[dy], j-dj[dy]
    
    if arr[bi][bj] != 1:
        dfs(bi, bj, dy)
        
    
N, M = map(int,input().split())
# 좌표 (r,c) 방향 d 0 1 2 3
r, c, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
cnt = 0
dfs(r,c,d)
print(cnt)