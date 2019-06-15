def karatsuba(x, y):
    '''
    Input: two n-digit positive integers x and y
    Output: multiplication of x and y
    Assumption: n is a power of 2
    '''
    x  = str(x)
    y = str(y)

    if len(str(x)) == 1 or len(str(y)) == 1:
	    return x*y

    n = max(len(str(x)), len(str(y)))
    nby2 = n//2

    a = int(x[:nby2])
    b = int(x[nby2:])
    c = int(y[:nby2])
    d = int(y[nby2:])

    ac = a*c
    bd = b*d
    p = (((a+b)*(c+d))-(ac + bd))

    final = (ac)*(10)**(2*nby2) + p * 10**(nby2) + bd

    return final

print(karatsuba(1000,2000))    
