def make_bricks(small, big, goal):
    if small + big*5 >= goal:
        if (goal % 5 - small) > 0:
            return False
        else:
            return True
    else:
        return False

