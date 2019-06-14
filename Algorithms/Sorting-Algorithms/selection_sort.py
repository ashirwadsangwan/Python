
def selectionSort(A):

    n = len(A)

    for i in range(n-1):
        i_min = i
        for j in range(i+1, n):
            if A[j] < A[i_min]:
                i_min = j
        
        temp = A[i]     ## Records ith position in temp
        A[i] = A[i_min] ## records min position at ith index
        A[i_min] = temp ## puts temp in i_min index

    return A

if __name__ == "__main__":
    A = [2,3,1,5,2,7,0,1]
    sorted_array = selectionSort(A)
    print(sorted_array)
