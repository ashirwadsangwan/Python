'''
Iterative
O(n)
'''
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


'''
Recurcive
O(n)
'''

def power(x, n):

    if n==0:
        return 1
    return x*power(x, n-1)

'''
More efficient Recurcive Program
O(log n)
'''
def power(x, n):

    if n==0:
        return 1

    elif n%2==0:
        y = power(x, n/2)
        return y*y

    return x*power(x, n-1)

print(power(3, 19))
