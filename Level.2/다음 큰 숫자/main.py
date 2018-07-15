def solution(n):
    binary_origin = format(n,'b')
    while True:
        n = n + 1
        binary_compare = format(n,'b')
        if binary_origin.count('1') == binary_compare.count('1'):
            return n