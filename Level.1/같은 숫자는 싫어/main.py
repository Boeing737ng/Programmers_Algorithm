def no_continuous(s):
    list = []
    # 함수를 완성하세요
    for i in range(len(s)):
        if i == 0:
            list.append(s[i])
        elif s[i] != s[i-1]:
            list.append(s[i])
    return list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))