class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        a = list(set(nums))
        a.sort()
        for i in range(len(a)):
            nums[i] = a[i]
        return len(set(nums))