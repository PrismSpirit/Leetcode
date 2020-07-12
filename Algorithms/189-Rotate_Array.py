class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = list(nums[:len(nums) - k])
        del nums[:len(nums) - k]
        nums.extend(tmp)