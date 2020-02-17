class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [num for num in str(int(''.join(map(str,digits)))+1)]