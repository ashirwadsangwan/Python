def power_of_two(x):
    if x == 1:
        return True
    if x < 1:
        return False
    return power_of_two(x / 2)
