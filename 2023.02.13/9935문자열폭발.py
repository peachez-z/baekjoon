stack = []
txt = list(input())
txt_s = list(input())
h = len(txt_s)
for i in range(len(txt)):
    # txt_s의 길이보다 stack이 작으면 계속 쌓기
    if len(stack) < h :
        stack.append(txt[i])
    # txt_s 보다 크거나 같아지면, 뒤에있는 문자열이 txt_s와 같은지 검사
    elif len(stack) >= h and stack[-len(txt_s):] == txt_s:
        # 같으면 txt_s의 길이 만큼 pop해서 삭제
        for _ in range(h):
            stack.pop()
        # 문자열 마저 넣기
        stack.append(txt[i])
    else:
        stack.append(txt[i])
# 마지막에 들어오는 문자열이 txt_s일때 안걸러져서 추가했음
# 스택의 마지막 문자열이 txt_s라면 pop 반복
if stack[-len(txt_s):] == txt_s:
    for _ in range(h):
        stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')