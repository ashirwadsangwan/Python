def peak(array):
    peaks = []
    
    if array[0]>array[1]:
        peaks.append(0)

    for i in range(1, len(array)-1):
        if array[i]>array[i-1] and array[i]>array[i+1]:
            peaks.append(i)

    if array[-1]>array[-2]:
        peaks.append(len(array)-1)

    return peaks

arr = [1,0,3,2,1,4,3,5,2,6]
print(peak(arr))