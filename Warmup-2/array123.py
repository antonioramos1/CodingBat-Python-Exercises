def array123(nums):
    array_list_string = []
    for number in nums:
        array_list_string.append(str(number))
    array_string = ''.join(array_list_string)
    return ('123' in array_string)

