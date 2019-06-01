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


	n = max(len(str(x)),len(str(y)))
	nby2 = n // 2

	a = int(x[:nby2])
	b = int(x[nby2:])
	c = int(y[:nby2])
	d = int(y[nby2:])

	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

    	# this little trick, writing n as 2*nby2 takes care of both even and odd n
	prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

	return prod

karatsuba(1000, 2000)
