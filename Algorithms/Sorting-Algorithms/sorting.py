List = [32, 22, 33, 44, 65, 2, 9, 10]


def bubbleSort(array):
    """
    input: array
    return: sorted array of integers
    """

    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertionSort(array):

    for i in range(1, len(array)):
        target = array[i]
        hole = i

        while hole > 0 and array[hole - 1] > target:
            array[hole] = array[hole - 1]

            hole = hole - 1
        array[hole] = target

    return array


if __name__ == "__main__":
    List = [32, 22, 33, 44, 65, 2, 9, 10]
    print(insertionSort(List))
