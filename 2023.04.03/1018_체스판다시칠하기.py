N, M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(N)]
cnts = []
for i in range(N-7):
    for j in range(M-7):
        # d1 = W로 시작할 때 / d2 = B로 시작할 때
        w_start, b_start = 0,0
        # 8칸씩 자르기
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 행과 열의 합이 짝수 == 시작 지점과 같다
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'B':
                        w_start += 1
                    if arr[a][b] != 'W':
                        b_start += 1
                # 행과 열의 합이 홀수 == 시작 지점과 다름
                else:
                    if arr[a][b] != 'W':
                        w_start += 1
                    if arr[a][b] != 'B':
                        b_start += 1
        cnts.append(w_start)
        cnts.append(b_start)
print(min(cnts))

