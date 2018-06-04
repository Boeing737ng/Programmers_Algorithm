def solution(a, b):
    if a == b:
        return a
    if a > b:
        a,b = b,a
    return sum(list(range(a,b+1)))