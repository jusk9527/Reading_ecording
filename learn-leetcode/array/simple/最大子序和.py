# bad
# 求出全部相加之和，然后max求最大
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        elif len(nums)==1:
            return nums[0]
        else:
            sums = []
            sum_num = 0
            for i in range(len(nums)):
                sums.append(nums[i])
                for j in range(len(nums)-i-1):
                    nums[i] = nums[i] +nums[i+j+1]
                    # print(sum_num)
                    sums.append(nums[i])
            return max(sums)



nums =  [-2,1]

solution = Solution()
res = solution.maxSubArray(nums)
print(res)

