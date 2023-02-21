from collections import deque
def bfs(y,x):
	y, x = q.popleft()
	visited[y][x] = 1



dy =[-1,]
N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
y, x = 0,0
q = deque()
q.append(y,x)
