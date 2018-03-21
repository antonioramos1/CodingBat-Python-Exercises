def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
  
    if len(a_lower) > len(b_lower):
        return a_lower.endswith(b_lower)
    return b_lower.endswith(a_lower)
  
    #can also use:
    #min_ab = min(len(a_lower), len(b_lower))
    #return a_lower[-min_ab:] == b_lower[-min_ab:]

