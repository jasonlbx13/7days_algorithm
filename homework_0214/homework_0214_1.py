class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2==[]:
            return
        i=j=k=0
        cache = nums1[:m]
        while k<m and j<n:
            if cache[k]>nums2[j]:
                nums1[i] = nums2[j]
                j+=1
            else:
                nums1[i] = cache[k]
                k+=1
            i+=1
        if k==m and j<n:
            while j<n:
                nums1[i] = nums2[j]
                i+=1
                j+=1
        if j==n and k<m:
            while k<m:
                nums1[i] = cache[k]
                i+=1
                k+=1