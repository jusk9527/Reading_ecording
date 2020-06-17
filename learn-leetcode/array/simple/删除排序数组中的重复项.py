# 使用下标标记的方法、如果后一个和前一个相同就删除前一个，其他的都往前移动，
# 如果不相同就下标往后移动如此往复
# good
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_index = 0
        while list_index < len(nums) - 1:
            if nums[list_index] == nums[list_index + 1]:
                nums.remove(nums[list_index])
            else:
                list_index += 1
        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
res = solution.removeDuplicates(nums)
print(res)


# 这个不符合就是：用了额外的空间。但是我还是推荐可以掌握下
# better
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for item in nums:
            if item not in seen:
                yield item
                seen.add(item)

solution = Solution()
res = solution.removeDuplicates(nums)
print(len(list(res)))


# 如果是一个字典呢？上面都是些列表的方法，如果是字典我们该如何使用呢？

class Solution(object):
    def removeDuplicates(self, nums, key=None):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for item in nums:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
solution = Solution()
res = solution.removeDuplicates(a, key=lambda d: (d['x'],d['y']))
print(len(list(res)))




