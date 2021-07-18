class circularSorted:
    def __init__(self, A):
        self.A = A

    def rotationCount(self):

        n = len(self.A)
        low = 0
        high = n - 1

        while low <= high:
            if self.A[low] <= self.A[high]:
                return low
            mid = (low + high) // 2
            next_ = (mid + 1) % n
            prev = (mid + n - 1) % n

            if self.A[mid] < self.A[next_] and self.A[mid] < self.A[prev]:
                return mid

            elif self.A[mid] <= self.A[high]:
                high = mid - 1
            elif self.A[mid] >= self.A[low]:
                low = mid + 1

        return -1


if __name__ == "__main__":

    A = [23, 28, 31, 38, 5, 6, 8, 10, 12]
    array = circularSorted(A)
    count = array.rotationCount()
    print("The array is rotated {} times".format(count))
