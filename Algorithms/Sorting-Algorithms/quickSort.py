def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


if __name__ == "__main__":

    array = [2, 3, 1, 44, 2, 3, 1, 33]
    print(partition(array, 0, 7))
