class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = int(a, base=2)
        k = int(b, base=2)
        # print(m)
        # print(k)
        # print(m+k)

        return str(bin(m+k))[2:]
a = "11"
b = "1"

solution = Solution()
res = solution.addBinary(a, b)
print(res)
# 100

