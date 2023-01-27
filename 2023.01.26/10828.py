import sys 
num = int(input())
temp = []

for i in range(num):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        temp.append(com[-1])
    elif com[0] == 'pop':
        if len(temp) == 0:
            print('-1')
        else :
            print(temp.pop())
    elif com[0] == 'size':
        print(len(temp))
    elif com[0] == 'empty':
        if len(temp) == 0:
            print(1)
        else :
            print(0)
    else :
        if len(temp) == 0:
            print(-1)
        else :
            print(temp[-1])
        

  