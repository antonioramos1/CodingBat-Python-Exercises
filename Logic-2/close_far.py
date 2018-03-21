def close_far(a, b, c):
    list = [a,b,c]
    sorted_list = sorted(list)
    if max(sorted_list) - sorted_list[1] >= 2 and sorted_list[1] - min(sorted_list) < 2:
        return True
    elif max(sorted_list) - sorted_list[1] < 2 and sorted_list[1] - min(sorted_list) >= 2:
        return True
    return False
