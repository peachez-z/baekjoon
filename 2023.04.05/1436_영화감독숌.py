N = int(input())
cnt = 0
start = 666
while True:
    # start를 문자열로 바꾼 것에 666이 있으면 cnt 증가
    if '666' in str(start):
        cnt += 1
    # N번째를 찾았으면 멈추기
    if cnt == N:
        print(start)
        break
    # N번쨰를 찾지못했으면 start 1씩 증가
    start += 1