# 리스트에 있는 숫자들을 빈 stack에 넣음
# if stack에 들어올 숫자가 stack에 있던 숫자보다 크면
# stack.pop()을 해주면서 스택에 가장 큰 숫자가 들어오도록 유지
# k 번만 지울 수 있음 k > 0 이상일 때 수행
# k 미만으로 지우고 끝나면, k개 만큼 지우고 출력
import sys
n , k = map(int, sys.stdin.readline().split())
# rstrip() 안쓰면 \n따라옴
nums = sys.stdin.readline().rstrip()
print(nums)
stack = []

for num in nums:
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))