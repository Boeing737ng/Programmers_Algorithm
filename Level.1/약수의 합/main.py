def solution(n):
    measure = []
    for i in range(1,n+1):
        if n%i == 0:
            measure.append(i)
    return sum(measure)