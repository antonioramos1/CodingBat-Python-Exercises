def make_chocolate(small, big, goal):
    big_bars = big * 5
    if goal > big_bars:
        goal_remaining = goal - big_bars
    else:
        goal_remaining = goal % 5
  
    if small >= goal_remaining:
        return goal_remaining
    return -1
