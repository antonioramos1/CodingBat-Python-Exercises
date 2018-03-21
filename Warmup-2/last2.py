def last2(str):
    if len(str) < 2:
        return 0
    else:
        if str[-2] == str[-1] and str[-1]*3 in str:
            return str.count(str[-2:]) -1 +1 
        return str.count(str[-2:]) -1

