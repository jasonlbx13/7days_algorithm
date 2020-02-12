class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length>1:
            k = k%length
            if k>0:
                nums.extend(nums[0:-k])
                for i in range(length-k):
                    nums.pop(0)