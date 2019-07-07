def peak(array):
    peaks = []

    if len(array)==0:
        return "The array has zero elements"
    elif len(array)==1:
        return [0]
    elif len(array)==2:
        peaks = [0,1]
        return peaks

    if array[0]>array[1]:
        peaks.append(0)

    for i in range(1, len(array)-1):
        if array[i]>array[i-1] and array[i]>array[i+1]:
            peaks.append(i)

    if array[-1]>array[-2]:
        peaks.append(len(array)-1)

    return peaks


if __name__ == "__main__":
    print(peak([1])) # when array has only one elements
    print(peak([1, 2])) # when array has two elements
    print(peak([1, 0, 3]))
    print(peak([1,0,2,1,3,2,5,2,6]))
