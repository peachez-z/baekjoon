N = int(input())
bag = 0
while N >= 0:
    if N % 5 == 0:
        bag += N // 5
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)

# # 젤 적게 들려면 큰거부터
# # 5로 나눈 나머지
# ans = 0
# total = []
# if N % 5 == 0 :
#     ans = N // 5
#     total.append(ans)
# if N % 3 == 0:
#     ans = N // 3
#     total.append(ans)
# if ans == 0 :
#     temp = 5
#     while temp != 0:
#         # N을 temp로 나눈 나머지가 있다면
#         if N % temp:
#             # 나머지가 3으로 쪼개지는지 확인해보자
#             three = N % temp
#         if three:
#             # 5로 나눈 나머지가 3으로 나누어 떨어지면
#             if three % 3 == 0:
#                 # ans = 5로 나눈 몫 + 3으로 나눈 몫
#                 ans = temp + (three//3)
#             # 안나눠떨어지면 , ,
#             else:
#
#
#
#
#

# total = 100
# five = N // 5
# while ans != 0:
#     if five == 0 or three == 0:
#         break
#     # five로 나눈 나머지가 있다면
#     if N % five:
#         three = N % five
#     # three가 있다 = 5로 나눴을 때 나머지가 있다
#     if three :
#         # 5로 나누어지고, 3으로 나눴을 때 나머지가 있다면
#         if three % 3:
#             ans = -1
#         else:
#     # 5로 나누면 끝난다
#     else:
#         ans = five
#
#
#
#
#         if three % 3:
#             print(-1)
#
#     ans = total