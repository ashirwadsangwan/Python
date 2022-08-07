def bubbleSort(A):

    n = len(A)

    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A


if __name__ == "__main__":
    A = [2, 3, 1, 5, 2, 7, 0, 1]
    sorted_array = bubbleSort(A)
    print(sorted_array)
