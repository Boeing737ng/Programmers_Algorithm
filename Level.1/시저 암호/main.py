def solution(s, n):
    answer = ''
    for char in s.split(" "):
        for i in range(len(char)):
            ascii_word = ord(char[i])
            caesar = ascii_word + n
            if char[i].isupper():
                if caesar > 90:
                    caesar = caesar - 26
            else:
                if caesar > 122:
                    caesar = caesar - 26
            answer += chr(caesar)
        answer += " "
    return answer[:-1]