class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        cap = 0
        left_max = []
        right_max = []
        lmax = 0
        rmax = 0
        i = 0
        j = len(height)-1
        while i<len(height):
            if lmax<height[i]:
                lmax = height[i]
            left_max.append(max(lmax,height[i])-height[i])
            i+=1
        while j>=0:
            if rmax<height[j]:
                rmax = height[j]
            right_max.append(max(rmax,height[j])-height[j])
            j-=1
        right_max = right_max[::-1]
        for k in range(len(height)):
            cap += min(left_max[k],right_max[k])
        return cap
