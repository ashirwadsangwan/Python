'''
The problem has a complexity of O(log n)
'''

def peakFinding(array):

    n = len(array)

    if n==1:
        return 0
    if array[n//2] < array[(n//2)-1]:
        peakFinding(array[:(n//2)])
    elif array[n//2] < array[(n//2)+1]:
        peakFinding(array[(n//2)+1:])
    else:
        return n//2

print(peakFinding([2,3,1,3,2,5]))
