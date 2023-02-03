n, K = map(int,input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]
            cnt += 1
            if cnt == K:
                print(nums[j], nums[j+1])
                break
if cnt < K :
    print(-1)