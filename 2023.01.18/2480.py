nums = list(map(int,input().split()))
total = 0

if nums[0] == nums[1] == nums[2] :
    total += 10000+(nums[0]*1000)
elif (nums[0] == nums[1] != nums[2] ) :
    total += 1000 + nums[0] * 100
elif (nums[0] == nums[2]!= nums[1]):
    total += 1000 + nums[0] * 100
elif (nums[1] == nums[2] != nums[0]):
    total += 1000 + nums[1] * 100
elif nums[0] != nums[1] != nums[2] :
    total += max(nums) * 100

print(total)
    