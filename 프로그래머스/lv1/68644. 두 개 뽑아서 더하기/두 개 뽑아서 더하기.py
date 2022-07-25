def solution(numbers):
    n_list=numbers
    answer = []
    for i in range(0,len(n_list)):
        for j in range(i+1,len(n_list)):
            answer.append(n_list[i]+n_list[j])

    result = list(set(answer))
    result.sort()
    return result


