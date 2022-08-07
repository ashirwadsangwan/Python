def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        value = A[i]
        hole = i

        while hole > 0 and A[hole - 1] > value:
            A[hole] = A[hole - 1]
            hole = hole - 1
        A[hole] = value
    return A


if __name__ == "__main__":
    A = [7, 10, 3, 1, 5, 2, 7, 0, 1]
    sorted_array = insertionSort(A)
    print(sorted_array)
