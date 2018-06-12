def solution(s):
    answer = ''
    s = [int(x) for x in str(s)]
    s.sort()
    s.reverse()
    answer = ''.join(str(x) for x in s)
    return int(answer)