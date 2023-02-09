import sys
txt = list(input())
n = int(input())
stack = []

for i in range(n):
    x = sys.stdin.readline().split()
    # 왼쪽으로 한칸 이동
    if x[0] == 'L' and cs > 0:
        cs -= 1
    # cs자리에 x[1] 추가
    elif x[0] == 'P':
        txt.insert(cs,x[1])
        cs += 1
    # 오른쪽으로 한칸 이동 / 커서가 맨뒤면 이동 X
    elif x[0] == 'D' and cs < len(txt):
        cs += 1
    elif x[0] == 'B' and cs > 0:
        txt.pop(cs-1)
        cs -= 1

for i in range(len(txt)):
    print(txt[i], end='')
