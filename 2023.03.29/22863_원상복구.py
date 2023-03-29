# n 카드개수 / k 섞은횟수
n, k = map(int,input().split())
# k번 섞은 상태
Si = list(map(int,input().split()))
# Di
Di = list(map(int,input().split()))

arr = []
for i in range(n):
    arr.append([Di[i],i])
# print(arr)
arr.sort()
# print(arr)

ans = [Si[i] for i in range(n)]
for i in range(k):
    temp = []
    for j in arr:
        temp.append(ans[j[1]])
        # print('temp',temp)
    for h in range(n):
        ans[h] = temp[h]
        # print('ans',ans)
print(*ans)