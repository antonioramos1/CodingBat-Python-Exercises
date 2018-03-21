def in1to10(n, outside_mode):
    if outside_mode == False:
        return 1 <= n < 11
    else:
        return (1 >= n or n>= 10)
