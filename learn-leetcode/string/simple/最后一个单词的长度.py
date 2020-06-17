class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.split():
            return len(s.split()[-1])
        else:
            return 0

s = "Hello World"
solution = Solution()
res = solution.lengthOfLastWord(s)
print(res)
# "Hello World"