class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if nums[j] == val:
                nums.remove(val)

            else:
                j = j+1

        return len(nums)

nums = [3,2,2,3]
val = 3
solution = Solution()
res = solution.removeElement(nums, val)
print(res)