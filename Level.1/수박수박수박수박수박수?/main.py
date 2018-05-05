def water_melon(n):
    # 함수를 완성하세요.
    result = ""
    for i in range(n):
        i += 1
        result += (i%2 == 0) and "박" or "수"
    return result


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))