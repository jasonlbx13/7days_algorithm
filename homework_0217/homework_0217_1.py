class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i>=0:
            digits[i]+=1
            if digits[i]<10:
                break
            else:
                digits[i] = 0
            i-=1
        if i==-1:
            digits[:]=[1]+digits[:]
        return digits