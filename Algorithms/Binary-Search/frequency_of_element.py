"""
The question is to find out the number of times the element occurs in the array.
"""
class BinarySearch:

    def __init__(self, A, x):
        self.sorted_A = sorted(A)
        self.A = A
        self.x = x

    def first_occ(self):

        n = len(self.sorted_A)
        start = 0
        end = n-1
        result = -1
        
        while (start<=end):
        
            mid  = (start + end)//2

            if self.x == self.sorted_A[mid]:
                result  = mid
                end = mid-1
            
            elif self.x > self.sorted_A[mid]:
                start = mid+1

            else : end = mid - 1
    
        return result


    def last_occ(self):

        n = len(self.sorted_A)
        start = 0
        end = n-1
        result = -1

        while (start<=end):
        
            mid  = (start + end)//2

            if self.x == self.sorted_A[mid]:
                result  = mid
                start = mid+1
            
            elif self.x > self.sorted_A[mid]:
                start = mid+1

            else : end = mid - 1
        
        return result

    def frequency(self):
    
        return self.last_occ() - self.first_occ() + 1

    def rotationCount(self):
        n = len(self.A)
        low = 0
        high = n-1

        while (low<=high):
            if self.A[low] <= self.A[high]: return low
            mid = (low+high)//2
            next_ = (mid+1)%n
            prev = (mid+n-1)%n

            if self.A[mid] < self.A[next_] and self.A[mid] < self.A[prev]: return mid

            elif self.A[mid] <= self.A[high]:
                high = mid-1
            elif self.A[mid] >= self.A[low]:
                low = mid+1
            
        return -1




if __name__ == "__main__":

    array = BinarySearch([23,28,31,38,5,6,8,10,12], 5)
    count = array.rotationCount()
    print(array.frequency())
    print(array.first_occ())
    print(array.last_occ())
    
    print("The array is rotated {} times".format(count))