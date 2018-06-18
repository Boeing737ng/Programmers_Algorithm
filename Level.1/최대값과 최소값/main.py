def solution(s):
    answer = ''
    s = s.split()
    results = list(map(int, s))
    answer += str(min(results)) + " "
    answer += str(max(results))
    return answer