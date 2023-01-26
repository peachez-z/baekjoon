num = int(input())
temp = []
answer = []
for i in range(num):
    n = int(input())
    temp.append(n)
    
a = temp.pop()
answer.append(a)

b = temp.pop()
answer.append(b)
  
print(temp)
print(answer)