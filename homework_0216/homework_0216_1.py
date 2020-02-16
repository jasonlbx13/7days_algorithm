class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        cap = 0
        hmax = max(height)
        lmax = 0
        rmax = 0
        m = height.index(hmax)
        i = 0
        j = len(height)-1
        while i<m:
            if lmax>height[i]:
                cap += lmax-height[i]
            else:
                lmax = height[i]
            i+=1
        while j>m:
            if rmax>height[j]:
                cap += rmax-height[j]
            else:
                rmax = height[j]
            j-=1
        return cap