import sys 
from collections import deque
num = int(sys.stdin.readline())
que =deque([])

for i in range(num):
    txt = sys.stdin.readline().split()
    if txt[0] =='push':
        que.append(txt[1])

    elif txt[0] == 'empty':
        if len(que) == 0:
            print(1)
        else : 
            print(0)

    elif txt[0] == 'size':
        print(len(que))
    
    elif txt[0] == 'front':
        if len(que) == 0:
            print(-1)
        else :
            print(que[0])

    elif txt[0] == 'back':
        if len(que) == 0:
            print(-1)
        else :
            print(que[-1])

    elif txt[0] == 'pop':
        if len(que) == 0 :
            print(-1)
        else :
            print(que[0])
            que.popleft()
        
        
