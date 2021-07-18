def merge(L, R, A=[]):

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:

            A[k] = L[i]
            i += 1

        else:

            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1

    return A


if __name__ == "__main__":
    L = [1, 2]
    R = [7, 8]
    print(merge(L, R, A=[]))
