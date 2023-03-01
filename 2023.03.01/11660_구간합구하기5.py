import sys
input = sys.stdin.readline
# N*N 크기 / M번 계산
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 누적합 구하기
pre_sum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + arr[i-1][j-1]

# 구간합 구하기
for _ in range(M):
    # (x1,y1) ~ (x2,y2) 합 구하기
    x1, y1, x2, y2 = map(int,input().split())
    print(pre_sum[x2][y2] - pre_sum[x1-1][y2] - pre_sum[x2][y1-1] + pre_sum[x1-1][y1-1])