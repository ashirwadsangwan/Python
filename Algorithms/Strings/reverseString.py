def reverse_str(string):
    str = list(string)
    new_str = ""
    for i in range(len(str)):
        new_str += str.pop()

    return new_str

    ## Alternative


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
