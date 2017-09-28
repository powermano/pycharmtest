# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# # class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         save = {}
#         length = 0
#         max1 = 0
#         for i in range(len(s)):
#             length += 1
#             if s[i] in save:
#                 count = 0
#                 length = length - 1
#                 if max1 < length:
#                     max1 = length
#                 save1 = {}
#                 for k ,j in save.items():
#                     if j>save[s[i]]:
#                         count += 1
#                         save1[k]=j
#                 save1[s[i]] = i
#                 save = save1
#                 length = count+1
#             save[s[i]] = i
#
#         return max(max1, length)


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = max1 = 0
        save = {}

        for i in range(len(s)):
            if s[i] in save and start <= save[s[i]]:
                start = save[s[i]] + 1
            else:
                max1 = max(max1, i - start + 1)

            save[s[i]] = i

        return max1

test = 'vddevf'
s = Solution()
max_length = s.lengthOfLongestSubstring(test)
print(max_length)


