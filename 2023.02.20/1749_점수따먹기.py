import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + nums[i-1][j-1] - arr[i-1][j-1]

ans = -400000001
for x1 in range(1, 1+N):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                ans = max(ans, arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1])
print(ans)
