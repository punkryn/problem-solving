def getIndex(bias):
    if (bias == 'code'): return 0
    elif (bias == 'date'): return 1
    elif (bias == 'maximum'): return 2
    return 3

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    filtered = []
    idx = getIndex(ext)
    for d in data:
        if d[idx] < val_ext:
            filtered.append(d)
    idx = getIndex(sort_by)
    filtered.sort(key=lambda x: x[idx])
    
    return filtered