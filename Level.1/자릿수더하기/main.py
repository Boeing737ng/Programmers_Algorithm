def sum_digit(number):
    string = str(number)
    result = 0
    for i in string:
        result += int(i)
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));