class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best = -10**5
        curr = -10**5

        
        for i in nums:
            curr = max(i, curr+i)
            best = max(best, curr)

        return best
            