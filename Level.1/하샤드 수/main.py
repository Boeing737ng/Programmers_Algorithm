def solution(x):
    sum_of_num = sum(int(x) for x in str(x))
    if x % sum_of_num != 0:
        return False
    return True