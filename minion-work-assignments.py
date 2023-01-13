def solution(data, n): 
    if len(data) >= 100:
        return
    
    # build frequency graph
    freq_dict = dict()
    for point in data:
        try:
            freq_dict[point] += 1
        except KeyError:
            freq_dict[point] = 0
    
    # build result
    result = list()
    for point in data:
        if freq_dict[point] < n:
            result.append(point)

    return result

# absolutely a way you can do this in one line, but this is pretty readable and dictionarys are the best structure