def sum67(nums):
    new_list = nums
    if new_list == []:
        return 0
    while 6 in new_list:
        index6 = new_list.index(6)
        index7 = new_list.index(7,new_list.index(6))+1
        del new_list[index6:index7]
    return sum(new_list)
