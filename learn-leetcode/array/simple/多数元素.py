

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common()[0][0]

nums = [3,2,3]
solution = Solution()
res = solution.majorityElement(nums)
print(res)


# 3