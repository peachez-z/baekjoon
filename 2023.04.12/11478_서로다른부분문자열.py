s = input()  # 문자열 입력받기
substrings = set()  # 중복을 제거한 부분 문자열 집합

# 모든 위치에서 시작하는 부분 문자열 찾기
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substrings.add(s[i:j])

print(len(substrings))  # 부분 문자열 개수 출력
