def DFS(value, answer):
    # n이 되면 멈추기
    if value == n:
        total.append(answer)
        print(total)
        return
    # 1을 더했을 때 n 이하면 answer에 1 추가하고 val+1 재귀
    if value + 1 <= n:
        DFS(value + 1, answer + [1])
    # 2을 더했을 때 n 이하면 answer에 2 추가하고 val+2 재귀
    if value + 2 <= n:
        DFS(value + 2, answer + [2])
    # 3을 더했을 때 n 이하면 answer에 3 추가하고 val+3 재귀
    if value + 3 <= n:
        DFS(value + 3, answer + [3])

n, k = map(int,input().split())
total = []
DFS(0, [])
# k 만큼 안돌아가면
if len(total) < k :
    print(-1)
# k 만큼 돌았으면
else:
    total = list(total)
    total.sort()
    answer = total[k-1]
    print(*answer, sep="+")