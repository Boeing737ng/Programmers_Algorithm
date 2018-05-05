def number_generator(x, n):
    # 함수를 완성하세요
    array = []
    for i in range(n):
        array.append((i+1)*x)
    return array

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))