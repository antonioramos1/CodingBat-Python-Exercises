def string_bits(str):
    new_str = ''
    for index, letter in enumerate(str):
        if index % 2 == 0:
            new_str += letter
    return new_str
