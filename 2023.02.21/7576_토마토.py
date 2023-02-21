from collections import deque

def bfs(y,x):
	while q:
		now_y, now_x = q.popleft()
		for k in range(4):
			ny, nx = now_y + dy[k], now_x + dx[k]
			if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
				arr[ny][nx] = arr[now_y][now_x] + 1
				q.append((ny,nx))
	return arr


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
M, N = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
q = deque([])
for i in range(N):
	for j in range(M):
		if arr[i][j] == 1:
			q.append((i,j))
ans = bfs(i,j)
maxV = 0
for lst in ans:
	if 0 in lst:
		print(-1)
		maxV = 0
		break
	else:
		if set(lst) == [1]:
			print(0)
			break
		else:
			for i in lst:
				if i > maxV:
					maxV = i
if maxV != 0:
	print(maxV-1)
