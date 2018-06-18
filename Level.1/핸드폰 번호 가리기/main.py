def solution(s):
    return s.replace(s[:-4],"*"*(len(s)-4))
