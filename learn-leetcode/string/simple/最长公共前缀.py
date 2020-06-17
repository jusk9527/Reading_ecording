class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
strs = ["flower","flow","flight"]
solution = Solution()
res = solution.longestCommonPrefix(strs)
print(res)


# fl