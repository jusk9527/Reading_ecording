class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = []
        m = []
        k = []
        for i in A:
            if i%2 ==1:
                l.append(i)
            else:
                m.append(i)
        for i in range(len(A)):
            if i%2 ==1:
                k.append(l.pop())
            else:
                k.append(m.pop())
        return k
A = [4,2,5,7]
solution = Solution()
res = solution.sortArrayByParityII(A)
print(res)

# [2, 7, 4, 5]