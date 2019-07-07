

def peakFinding(arr):
    '''
    The motive of this algorithm is find the first peak in the array
    and show its index.
    '''

    if len(arr)==1:
        return [0]

    elif len(arr)==2:
        return [0] if arr[0]>arr[1] else [1]

    else:
        if arr[0]>arr[1]:
            return [0]
        elif arr[0]<arr[1]:
            for i in range(3, len(arr)-1):
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    return [i] # returns the first index when finds a peak.
                else:
                    return [len(arr)-1]


if __name__ == "__main__":
    print(peakFinding([1])) # when array has only one elements
    print(peakFinding([1, 2])) # when array has two elements
    print(peakFinding([1, 0, 3]))
    print(peakFinding([1,0,2,1,3,2,5,2,6]))
    print(peakFinding([0,1,2,3,4,5]))
