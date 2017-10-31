class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        p = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                pass
