def alpha_string46(s):
    #함수를 완성하세요
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )