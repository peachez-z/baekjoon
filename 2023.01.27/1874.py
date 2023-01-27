n = int(input())
stack, ans, find = [], [], True

# 스택의 오름차순 성질 이용, 1부터 시작
now = 1

for i in range(n):
    num = int(input())
    # push
    while now <= num :
        # 스택은 1234 오름차순으로 쌓이기 때문에
        # 앞에 수보다 입력값이 커야 쌓을 수 있음
        stack.append(now)
        ans.append('+')
        now += 1
    # pop
    if stack[-1] == num :
        stack.pop()
        ans.append('-')
    # 불가능할 때
    else :
        find = False

if find == False :
    print('NO')
else :
    for i in ans:
        print(i)