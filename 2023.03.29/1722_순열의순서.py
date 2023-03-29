def per(n):
    if n in total:
        return total[n]
    elif n <= 1:
        return 1
    else:
        total[n] = n*per(n-1)
        return total[n]

n = int(input())
numbers = list(map(int,input().split()))
total = {}
# 첫번째 순열 만들기
arr = [i for i in range(1, n + 1)]

# k
if numbers[0] == 1:
    k = numbers[1]
    ans = []
    for i in range(n):
        x = per(n - 1 - i)
        order = (k-1) // x
        ans.append(arr[order])
        arr.remove(arr[order])
        k -= x*order
    print(*ans)

# 순열일 때
else:
    # 입력 받은 순열
    input_per = numbers[1:]
    ans = 1
    for i in range(n):
        order = arr.index(input_per[i])
        arr.remove(input_per[i])
        x = per(n-1-i)
        ans += x*order
    print(ans)




