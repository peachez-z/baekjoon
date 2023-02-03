import sys
n = int(sys.stdin.readline())
cnt = [0]*10001

for i in range(n):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):
    # cnt가 있을 때
    if cnt[i] > 0:
        # cnt된 횟수만큼 cnt의 인덱스를 출력
        for j in range(cnt[i]):
            print(i)