class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length>1:
            pre = nums[0]
            i = 1
            while i<length:
                if nums[i]==pre:
                    nums.pop(i)
                    length -= 1
                else:
                    pre = nums[i]
                    i += 1
        return length