class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = "".join(filter(str.isalnum,str(s))).lower()
        return m==m[::-1]

s = "A man, a plan, a canal: Panama"
solution = Solution()
res = solution.isPalindrome(s)
print(res)
# True


# 突发奇想的9*9乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s * %s =  %s  ' %(i,j,i*j),end="")
#     print()
