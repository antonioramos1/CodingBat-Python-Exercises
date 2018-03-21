def has22(nums):
    nums_string_list = []
    for number in nums:
        nums_string_list.append(str(number))
    nums_string = ''.join(nums_string_list)
    return ('22' in nums_string)
