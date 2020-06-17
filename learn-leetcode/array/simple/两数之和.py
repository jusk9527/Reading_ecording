# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# bad
class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:   List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums))[i+1:]:
                if nums[i] + nums[j] == target:
                    return [i, j]

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
rs = solution.twoSum(nums,target)
print(rs)
# [0, 1]
# 时间复杂度O(n*n)


# good

class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:   List[int]
        """
        hashmap = {}
        for k, v in enumerate(nums):
            hashmap[v] = k

        for key,values in enumerate(nums):
            m = target-values
            if m in hashmap:
                return [key,hashmap[m]]

solution = Solution()
rs = solution.twoSum(nums,target)
print(rs)
# [0, 1]
# 时间复杂度O(2*n)

# better
class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:   List[int]
        """
        hashmap = {}
        for key,values in enumerate(nums):
            m = target-values
            if m in hashmap:
                return [hashmap[m],key]
            hashmap[values] = key

solution = Solution()
rs = solution.twoSum(nums,target)
print(rs)
# [0, 1]
# 时间复杂度O(n)