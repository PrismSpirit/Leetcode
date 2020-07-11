class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if(target == nums[i] + nums[j]):
                    return_list.append(i)
                    return_list.append(j)
                    break
        return return_list