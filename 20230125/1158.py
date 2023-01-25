total, num= map(int,input().split())

# 처음에 의자에 있는 사람
temp = []
for i in range(total):
    temp.append(i+1)

# 빠진 수들
pops =[]
# 제거할 인덱스
idx = 0

for i in range(total):
    idx += num-1
    if idx >= len(temp):
        idx = idx%len(temp)
    pops.append(str(temp.pop(idx)))
    
print("<",", ".join(pops),">",sep='')

