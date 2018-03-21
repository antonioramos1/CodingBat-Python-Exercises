def string_splosion(string):
    splosion = ''
    for i in range(len(string)+1):
        splosion = splosion + string[0:i]
    return splosion
