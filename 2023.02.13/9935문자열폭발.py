stack = []
txt = list(input())
txt_s = list(input())
h = len(txt_s)
for i in range(len(txt)):
    if len(stack) < h :
        stack.append(txt[i])
    elif len(stack) >= h and stack[-len(txt_s):] == txt_s:
        for _ in range(h):
            stack.pop()
        stack.append(txt[i])
    else:
        stack.append(txt[i])

if stack[-len(txt_s):] == txt_s:
    for _ in range(h):
        stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')