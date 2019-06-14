
def rotationCount(A):

    n = len(A)
    low = 0
    high = n-1

    while (low<=high):
        if A[low] <= A[high]: return low
        mid = (low+high)//2
        next_ = (mid+1)%n
        prev = (mid+n-1)%n

        if A[mid] < A[next_] and A[mid] < A[prev]: return mid

        elif A[mid] <= A[high]:
            high = mid-1
        elif A[mid] >= A[low]:
            low = mid+1
        
    return -1


if __name__ == "__main__":

    A = [23,28,31,38,5,6,8,10,12]
    count = rotationCount(A)
    print("The array is rotated {} times".format(count))

