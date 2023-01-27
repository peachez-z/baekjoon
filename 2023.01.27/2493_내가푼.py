# li = [6, 9, 5, 7, 4]
num = int(input())
li = list(map(int,input().split()))
temp = []
ans =[]

for j in range(len(li)):
    # 첫번째 숫자는 무조건 0
    flag = True
    for i in range(j-1, -1, -1):
        if li[i] > li[j]:
            flag = False
            ans.append(i+1)
            break
    if flag:
        ans.append(0)
 
print(*ans)
