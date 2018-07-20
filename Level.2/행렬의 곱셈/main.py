def solution(arr1, arr2):
    answer = []
    len_arr2_row = len(arr2[0])
    for i in range(len(arr1)):
        row = []
        for j in range(len_arr2_row):
            temp = 0
            for k in range(len(arr1[i])):
                temp += arr1[i][k]*arr2[k][j]
            row.append(temp)
        answer.append(row)
    return answer