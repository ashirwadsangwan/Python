List = [32, 22, 33, 45, 2, 4, 10, 9]

def insertionSort(array):

    '''
    input: array of integers
    return : sorted array
    '''
    for i in range(1, len(array)):
        target = array[i]
        hole  = i

        while (hole>0 and array[hole-1]>target):
            array[hole] = array[hole-1]
            hole = hole - 1
        array[hole] = target
    
    return array


if __name__ == "__main__":
    List = [32, 22, 33, 45, 2, 4, 10, 9]
    print(insertionSort(List))



