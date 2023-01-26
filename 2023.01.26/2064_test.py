num = int(input())

if num < 4 :
    print(2)
elif num == 4 :
    print(4)

# num > 4 이상일 때 부터 시작
elif num > 4:
    # 짝수
    if num % 2 == 0:
        if num % 4 == 0 :
            print(8)
        else :
            print(4)
    # 홀수
    elif num % 2 == 1:
        if num % 4 == 1:
            print(2)
        else:
            print(6)