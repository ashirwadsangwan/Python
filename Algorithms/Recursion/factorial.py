def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Alternatively
"""


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
