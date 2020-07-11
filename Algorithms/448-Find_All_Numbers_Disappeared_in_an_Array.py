class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l1 = set(nums)
        l2 = set(x for x in range(1, len(nums) + 1))
        
        l3 = l2 - l1
        
        return l3