import itertools

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        for x in list(itertools.combinations((nums), 2)):
            if x[0] == x[1]:
                count += 1
                
        return count