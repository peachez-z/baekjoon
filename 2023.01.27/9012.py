n = int(input())

for i in range(n):
    x = list(input())
    stack = []
    for i in range(len(x)):
        if x[i] == '(':
            stack.append(x[i])
        else :
            if len(stack) != 0:
                stack.pop()
            else :
                print('NO')
                break
    else : 
        if len(stack) == 0:
            print('YES')
        else :
            print('NO')

