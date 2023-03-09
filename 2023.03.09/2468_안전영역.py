import sys 
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,-1,0,1]

def dfs(i,j,h):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] > h:
            visited[ni][nj] = True
            dfs(ni, nj, h)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxV = 0
for lst in arr:
    for num in lst:
        if maxV < num:
            maxV = num
ans = 0
for h in range(maxV):
    visited = [[False]*N for _ in range(N)]
    safe = 0  
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j]==False:
                safe += 1
                visited[i][j] == True
                dfs(i, j, h)
    if safe > ans:
        ans = safe
print(ans)
    