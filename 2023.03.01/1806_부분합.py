import sys
input = sys.stdin.readline
# 길이 N 수열의 합이 S 이상이 되는 가장 짧은 것의 길이
N, S = map(int,input().split())
numbers = list(map(int,input().split()))
pre_sum = [0]*(N+1)
for i in range(1,len(pre_sum)):
    pre_sum[i] = pre_sum[i-1] + numbers[i-1]
print(pre_sum)

# 구간 설정
start = 0
end = 1
# N은 100000이하의 자연수
ans = 100001
# 시작 지점이 끝이 아닐 때
while start != N:
    # 특정 구간합이 S 이상일 때
    if pre_sum[end] - pre_sum[start] >= S:
        # 구간이 최대 ans 보다 작을 때
        if end - start < ans:
            # ans 는 구간이 된다
            ans = end - start
        # 시작 지점 뒤로 밀어서 구간 점점 줄이기
        start += 1
    # 특정 구간합이 S 보다 작을 때
    else:
        # end가 끝까지 안갔으면 end 증가
        if end != N:
            end += 1
        # end가 끝이면 start 증가
        else:
            start += 1
# 답이 있을 경우
if ans != 100001:
    print(ans)
else:
    print(0)

