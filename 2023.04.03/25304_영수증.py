total = int(input())
N = int(input())
won = 0
for _ in range(N):
    a, b = map(int,input().split())
    won += a*b
if won == total :
    print('Yes')
else:
    print('No')