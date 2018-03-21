def missing_char(str, n):
    if str != '' and n <= len(str)-1:
        return (str[:n] + str[n+1:])
    else:
       return 'error'
