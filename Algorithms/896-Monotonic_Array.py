class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase = True
        decrease = True
        
        for x in range(0, len(A) - 1):
            if A[x] > A[x + 1]:
                increase = False
            if A[x] < A[x + 1]:
                decrease = False
                
        return increase or decrease