class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for key,values in enumerate(nums):
                if values > target:
                    return key
            return len(nums)

nums = [1,3,5,6]
target = 5
solution = Solution()
res = solution.searchInsert(nums, target)
print(res)