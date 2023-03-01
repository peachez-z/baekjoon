import sys
input = sys.stdin.readline
# N - 수의 개수 / M - 구해야하는 횟수
N, M = map(int,input().split())
numbers = list(map(int,input().split()))
pre_sum = [0]*(1+len(numbers))
for i in range(1,len(pre_sum)):
    pre_sum[i] = numbers[i-1] + pre_sum[i-1]
for _ in range(M):
    start, end = map(int,input().split())
    print(pre_sum[end] - pre_sum[start-1])