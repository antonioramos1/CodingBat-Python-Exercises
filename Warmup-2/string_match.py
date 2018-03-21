def string_match(a, b):
    counter = 0
    len_ab = min(len(a), len(b))
  
    for index in range(len_ab -1):
        if a[index:index+2] == b[index:index+2]:
            counter += 1
    return counter

