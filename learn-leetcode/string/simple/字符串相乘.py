num1 = "2"
num2 = "3"

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = 10
        max_num1_len = len(num1) -1
        max_num2_len = len(num2) - 1

        num1_sum = 0
        num2_sum = 0
        # 循环次数
        for i in range(len(num1)):
            num1_sum = (int(num1[i])*(m**(max_num1_len-i)))+num1_sum

        # print(num1_sum)

        for j in range(len(num2)):
            num2_sum = (int(num2[j])*(m**(max_num2_len-j)))+num2_sum

        # print(num2_sum)

        return str(num1_sum*num2_sum)


num1 = "123"
num2 = "456"
solution = Solution()
res = solution.multiply(num1, num2)
print(res)