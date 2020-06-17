class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = "".join('%s' %id for id in digits)
        target = int(digit)+1
        return [int(i) for i in list(str(target))]
digits = [4,3,2,1]
solution = Solution()
res = solution.plusOne(digits)
print(res)