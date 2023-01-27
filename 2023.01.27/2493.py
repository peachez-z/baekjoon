num = int(input())
li = list(map(int,input().split()))
stack = []
ans = [0]*num
for i in range(num):
    if stack :
        while True:
            if li[i] <= stack[-1][0]:
                ans[i] = stack[-1][1] + 1
                stack.append([li[i], i])
                break
            else : 
                stack.pop()
            if not stack :
                stack.append([li[i], i])
                break
    else:
        stack.append([li[i], i])

print(*ans)