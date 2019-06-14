"""
The question is to find out the number of times the element occurs in the array.
"""
class BinarySearch:

    def __init__(self, A, x):
        self.A = sorted(A)
        self.x = x

    def first_occ(self):

        n = len(self.A)
        start = 0
        end = n-1
        result = -1
        
        while (start<=end):
        
            mid  = (start + end)//2

            if self.x == self.A[mid]:
                result  = mid
                end = mid-1
            
            elif self.x > self.A[mid]:
                start = mid+1

            else : end = mid - 1
    
        return result


    def last_occ(self):

        n = len(self.A)
        start = 0
        end = n-1
        result = -1

        while (start<=end):
        
            mid  = (start + end)//2

            if self.x == self.A[mid]:
                result  = mid
                start = mid+1
            
            elif self.x > self.A[mid]:
                start = mid+1

            else : end = mid - 1
        
        return result

    def frequency(self):
    
        return self.last_occ() - self.first_occ() + 1

    



if __name__ == "__main__":

    array = BinarySearch([23,28,31,38,5,5,5,5,6,8,10,12], 5)
    
    print(array.frequency())
    print(array.first_occ())
    print(array.last_occ())
    
    