class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lmax = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                lmax = max(lmax, self.isValid(s[i:j + 1]))
        return lmax

    def isValid(self, s):
        res = []
        count = 0
        dict = {'(': ')'}
        for i in s:
            if i in dict:
                res.append(i)
                count += 1
            elif i in dict.values():
                if res == [] or dict[res.pop()] != i:
                    return 0
        if res == []:
            return count * 2
        else:
            return 0

# a = Solution()
# test = '(()))())('
# b = a.longestValidParentheses(test)
# print(b)

class Solution1:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
                if (i - dp[i - 1] - 2) < 0:
                    dp[i] = dp[i - 1] + 2
                else:
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)

test = '(()))())('
a1 = Solution1()
print(a1.longestValidParentheses(test))