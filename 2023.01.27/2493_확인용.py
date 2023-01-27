num = 5
li = [6, 9, 5, 7, 4]
stack = []
ans = [0]*num
for i in range(num):
    print('i :',i)
    # 스택이 있을 때
    if stack :
        while True:
            # li[i]가 stack에 들어있는 마지막 값보다 작을 때
            if li[i] <= stack[-1][0]:
                print(f'li[i] :{li[i]} 가 앞에 값보다 작다')
                # 더큰 stack의 마지막 값의 인덱스+1을 ans에 추가
                ans[i] = stack[-1][1] + 1
                print(f'ans{ans[i]} 에 {stack[-1][1] + 1} 추가')
                stack.append([li[i], i])
                print(stack)
                print('-'*50)
                break

            # li[i]가 stack에 있는 값보다 클 때
            # stack에서 그 값을 지움
            else : 
                print(f'li[i] :{li[i]} 가 앞에 값보다 크다')
                print('pop전',stack)
                stack.pop()
                print('pop후',stack)
                print('-'*50)

            # 다 지워져서 스택이 없다면 그 li[i]를 스택에 추가
            if not stack :
                print('스택이 다지워짐')
                stack.append([li[i], i])
                print(stack)
                print('-'*50)
                break
    # 스택이 없을 때 = 첫 숫자
    else:
        stack.append([li[i], i])
        print(stack)
        print('-'*50)


print(ans)