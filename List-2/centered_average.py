def centered_average(nums):
    new_list = nums
    new_list.remove(max(new_list))
    new_list.remove(min(new_list))
    return sum(new_list)//len(new_list) 
