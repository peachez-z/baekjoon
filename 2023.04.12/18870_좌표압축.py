n = int(input())  # 수열의 길이 입력받기
a = list(map(int, input().split()))  # 수열 입력받기

# 정렬된 수열에서 중복된 숫자 제거하기
sorted_a = sorted(set(a))

# 각 숫자가 몇 번째로 작은 숫자인지 구하기
index_dict = {sorted_a[i]: i for i in range(len(sorted_a))}

# 각 숫자의 인덱스 출력하기
for x in a:
    print(index_dict[x], end=' ')
