class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = list()
        sorted_nums = sorted(nums)
        
        for x in nums:
            output.append(sorted_nums.index(x))
            
        return output