class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lower = 0
        upper = len(nums) -1
        
        
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] < target:
                lower = mid +1
            elif nums[mid] > target:
                upper = mid -1
            else:
                return mid
            
        return lower                
            