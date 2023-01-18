hr, min = map(int,input().split())
plus = int(input())

hr += plus // 60
min += plus%60

if min >= 60:
    hr += 1
    min -= 60
if hr >= 24:
    hr -= 24

print(hr,min)