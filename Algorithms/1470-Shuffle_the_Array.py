class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = list()
        
        for x in range(0, n):
            shuffled.append(nums[0 + x])
            shuffled.append(nums[n + x])
            
        return shuffled