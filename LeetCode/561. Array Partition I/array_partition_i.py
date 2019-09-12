class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = sorted(nums)
        return sum([s[i] for i in range(0, len(s), 2)])
        
        
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
