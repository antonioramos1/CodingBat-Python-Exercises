def sum13(nums):
    new_list = nums
    while 13 in new_list:
        if new_list[-1] == 13:
            del new_list[-1]
        else:
            del new_list[new_list.index(13)+1], new_list[new_list.index(13)]
    return sum(new_list)
