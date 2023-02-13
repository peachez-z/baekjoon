N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
print(arr)
# 시작점
x , y = 1, 1
cnt = 0
while x != M  and y != N :

    # 아래로 내려가기
    if y < N and arr[y+1][x] == 1 and visited[y+1][x]== False and y != 3:
        y += 1
        cnt += 1
        visited[y][x] = True
    elif y < N and arr[y-1][x] == 1 and visited[y-1][x] == False and y != 0:
        y -= 1
        cnt += 1
        visited[y][x] = True
    elif x < M and arr[y][x+1] == 1 and visited[y][x+1] == False and x != 5:
        x += 1
        cnt += 1
        visited[y][x] = True
    elif x < M and arr[y][x-1] == 1 and visited[y][x+1] == False and x != 0:
        x -= 1
        cnt += 1
        visited[y][x] = True

print(cnt)

