from collections import deque
def bfs(friends, start):
    num = [0]*(N+1)
    visited = [0]*(N+1)
    visited[start] = 1
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        for i in friends[now]:
            if visited[i] == 0:
                num[i] = num[now] + 1
                visited[i] = 1
                que.append(i)
    return sum(num)

N, M = map(int,input().split())
friends = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
ans = []
for i in range(1,N+1):
    ans.append(bfs(friends,i))
print(ans.index(min(ans))+1)