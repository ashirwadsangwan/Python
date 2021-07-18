def binarySearch(A, low, high, x):
    """
    A: Array
    low: start of your array
    high: end of your array
    x: the element you're looking for
    """
    A = sorted(A)

    mid = (low + high) // 2

    if x == A[mid]:
        return mid
    elif x > A[mid]:
        return binarySearch(A, mid + 1, high, x)
    elif x < A[mid]:
        return binarySearch(A, low, mid - 1, x)
    else:
        return "x does not exist in A"


print("x is at index: ", binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 2))
