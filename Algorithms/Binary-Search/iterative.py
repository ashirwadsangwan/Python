def binarySearch(A, x):
    """
    A: Array
    n: Length of the array
    x: The element we're looking for
    """
    A = sorted(A)

    n = len(A)
    start = 0
    end = n - 1

    while start <= end:

        mid = (start + end) // 2

        if x == A[mid]:
            return mid

        elif x > A[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return "x is not in A"


print(
    "The number x is at index {}".format(
        binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
    )
)
