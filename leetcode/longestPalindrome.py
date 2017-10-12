# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.


# # import numpy as np
# class Solution(object):
#         def longestPalindrome(self, s):
#             """
#                    :type s: str
#                    :rtype: str
#             """
#             length =len(s)
#             rs = None
#             # p = np.zeros((length, length),dtype=int)
#             p = [[0 for x in range(length)] for y in range(length)]
#             for i in range(length)[::-1]:
#                 for j in range(i,length):
#                     if s[i]==s[j] and (j-i<2 or p[i+1][j-1]==1):
#                         p[i][j]=1
#
#                     if p[i][j]==1 and (rs==None or j-i+1>len(rs)):
#                         rs = s[i:j+1]
#             return  rs
#
#
#
# a = Solution()
# b=a.longestPalindrome('cbbdb')
# print(b)

class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        else:
            return self.findCommandSubstring(s,s[::-1])


    def findCommandSubstring(self,s1,s2):
        m, n, max_length,final_str = len(s1), len(s2), 0, None
        p=[[0]*n for j in range(m)]
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0) and s1[i]==s2[j]:
                    p[i][j]=1
                if i>0 and j>0 and s1[i]==s2[j]:
                    p[i][j]=p[i-1][j-1]+1
                # max_length = max(max_length,p[i][j])
                # if p[i][j]>0 and (str==None or p[i][j]>len(str)):
                #     str = s1[(i-p[i][j]+1):i+1]
                if p[i][j]>1:
                    str = s1[(i - p[i][j] + 1):i + 1]

                    flag =True
                    for k in range(len(str)//2):
                        if str[k]!=str[len(str)-1-k]:
                            flag=False
                            break
                    if flag and (final_str==None or len(str)>len(final_str)):
                            final_str=str
        if final_str==None:
            return s1[0]
        return  final_str


# s1='abc'
# s2='cabdf'
# print(findCommandSubstring(s1, s2))

test="abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
s = Solution()
print(s.longestPalindrome(test))





