import sys

txt = list(sys.stdin.readline())
cnt = int(sys.stdin.readline())
n = len(txt)
while cnt != 0:
    x = sys.stdin.readline()
    if 'P' in x:
        txt.insert(n,x[-1])
        # 하나가 추가됐기 때문에 자리 하나 추가
        n += 1
    # 맨 앞에 있는게 아니라면, 앞으로 1칸 이동
    elif 'L' in x and n > 0:
        n -= 1
    # 맨 뒤에 있는게 아니라면, 뒤로 1칸 이동
    elif 'D' in x and n < len(txt):
        n += 1
    # 첫번째 자리가 아니면, 앞에 값을 삭제
    elif 'B' in x and n > 0:
        del txt[n-1]
        # 값이 삭제 됐으니 커서 1칸 당기기
        n -= 1
    cnt -= 1

print(''.join(txt))



# for i in range(n+1, 0, -1):
#     x = input()
#     if 'P' in x:
#         print('i',i)
#         txt.insert(i,x[-1])
#         print(txt)
#     # 왼쪽으로 한칸 이동
#     elif 'L' in x:
#         print('i', i)
#         i -= 1
#     # 오른쪽으로 한칸 이동 / 커서가 맨뒤면 이동 X
#     elif 'D' in x:
#         if i != len(txt):
#             i += 1
#     elif 'B' in x:
#         print('i', i)
#         del txt[i-1]
