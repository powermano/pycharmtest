## the problems
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         solution = []
#
#         for i in range(len(nums) - 1):
#
#             for j in range(i + 1, len(nums)):
#
#                 if nums[i] + nums[j] == target:
#
#                     solution.append(i)
#                     solution.append(j)
#
#         return solution


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


nums = [11, 7, 2, 15]
target = 9
a = Solution()
b = a.twoSum(nums, target)
print(b)

