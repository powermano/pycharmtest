# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         nums.sort()
#         for i in range(len(nums)-1):
#             # if i>0 and (nums[i]==nums[i+1]):
#             #     continue
#             l = i+1
#             r = len(nums)-1
#             while l<r:
#                 sums = nums[i]+nums[l]+nums[r]
#                 if sums>0:
#                     r-=1
#                 elif sums<0:
#                     l+=1
#                 else:
#                     if len(result)>0:
#                         same = True
#                         for j in range(len(result)):
#                             if nums[i]==result[j][0] and nums[l]==result[j][1] and nums[r]==result[j][2]:
#                                 same = False
#                         if same == True:
#                             result.append([nums[i], nums[l], nums[r]])
#                     else:
#                         result.append([nums[i], nums[l], nums[r]])
#                     # if nums[l+1]==nums[l]:
#                     #     l+=1
#                     # if nums[r]==nums[r-1]:
#                     #     r-=1
#                     l += 1; r -= 1
#         return result



class Solution(object):
    def threeSum(self, nums):
        '''
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
        '''
        # method 2: split into positive and negtive
        res = []
        counter = {}
        for e in nums:
            if e in counter:
                counter[e] += 1
            else:
                counter[e] = 1

        values = counter.keys()
        pos = [n for n in values if n >= 0]
        neg = [n for n in values if n < 0]
        # three 0 case
        if 0 in values and counter[0] > 2:
            res.append((0, 0, 0))
        # pos + neg + target case
        for x in range(len(pos)):
            # if x > 0 and pos[x] == pos[x - 1]:
            #     continue
            for y in neg:
                target = -(pos[x] + y)
                if target in counter:
                    if (target == pos[x] or target == y) and counter[target] > 1:
                        res.append((target, pos[x], y))
                    elif (target < pos[x] or target < y):
                        res.append((target, pos[x], y))
        return res


a=Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
