class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length>1:
            k = k%length
            nums.reverse()
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:])