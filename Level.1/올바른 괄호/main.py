def solution(s):
    answer = True
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            try:
                stack.pop()
            except:
                return False
    return len(stack) == 0