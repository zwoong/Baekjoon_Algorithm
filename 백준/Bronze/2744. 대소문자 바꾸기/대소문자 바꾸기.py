str = input()

result = ""

for s in str:
    # 대소문자 체크
    if s.isupper():
        result += s.lower()
    else:
        result += s.upper()

print(result)