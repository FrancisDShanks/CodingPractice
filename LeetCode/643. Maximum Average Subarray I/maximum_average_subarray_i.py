class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k > len(nums) :
            return 0
        res = sum(nums[:k])
        m = res  # initial m as the sum of first subarray. in case of the array only has one element and the loop is not executed.
        for i in range(1, len(nums) - k + 1):
            res = res - nums[i - 1] + nums[i + k - 1]
            if res > m:
                m = res
        return m /  k
