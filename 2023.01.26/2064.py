from collections import deque

num = int(input())
temp = deque([])

for i in range(num) :
    temp.append(i+1)

while len(temp) > 1:
    temp.popleft()
    pops = temp.popleft()
    temp.append(pops)


print(temp[0])