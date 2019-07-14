'''
Time complexity : O(log n)
'''
def mod_exp(x, n, m):

    if n==0:
        return 1

    elif n%2==0:
        y = mod_exp(x, n/2, m)
        return (y*y)%m

    return ((x%m)* mod_exp(x, n-1, m))%m
