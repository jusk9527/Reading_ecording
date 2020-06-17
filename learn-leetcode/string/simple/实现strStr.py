class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        c=-1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                c=i
                break
        return c
haystack = "hello"
needle = "ll"
solution = Solution()
res = solution.strStr(haystack, needle)
print(res)
# 2