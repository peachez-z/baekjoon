N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
print(arr)
# 시작점
x , y = 0, 0
cnt = 0
print(visited)
while x != M and y != N:
    # 내려가기
    if y < N-1 and arr[y+1][x] == 1 and visited[y+1][x] == False:
        y += 1
        cnt += 1
        print('1','y','x','cnt',y,x,cnt)
        visited[y][x] = True
    # 위로 올라가기
    elif arr[y-1][x] == 1 and visited[y-1][x] == False and y != 0:
        y -= 1
        cnt += 1
        print('2', 'y', 'x', 'cnt', y, x, cnt)
        visited[y][x] = True
    elif x < M-1 and arr[y][x+1] == 1 and visited[y][x+1] == False:
        x += 1
        cnt += 1
        print('3', 'y', 'x', 'cnt', y, x, cnt)
        visited[y][x] = True
    elif x < M-1 and arr[y][x-1] == 1 and visited[y][x-1] == False :
        x -= 1
        cnt += 1
        print('4', 'y', 'x', 'cnt', y, x, cnt)
        visited[y][x] = True
    if x == (M-1) and y == (N-1) :
        break

print(cnt+1)

