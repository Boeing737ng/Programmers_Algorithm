def solution(s):
    s = s.lower()
    if s.count('p') == 0 and s.count('y') == 0:
        return True
    if s.count('p') != s.count('y'):
        return False
    else:
        return True