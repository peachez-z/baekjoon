def fib(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    else :
        cnt += 1
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    f=[0]*(n+1)
    f[1],f[2] == 1,1
    cnt = 0
    for i in range(3, n+1):
        cnt += 1
        f[i] = f[i-1] + f[i-2]
    return cnt

n = int(input())
cnt = 1
print(f'{fib(n)} {fibonacci(n)}')