def solution(s):
    answer = ''
    words = s.lower().split(" ")
    for i in words:
        for j,char in enumerate(i):
            if j % 2 == 0:
                char = char.upper()
            answer += char
        answer += " "
    return answer[:-1]