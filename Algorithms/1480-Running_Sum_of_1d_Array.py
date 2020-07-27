class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = list()
        tmp = 0
        
        for x in nums:
            tmp += x
            output.append(tmp)
        
        return output