class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return  results


    def findNsum(self, nums, target, N, result, results):
        if len(nums)< 2 or N < 2:
            return []
        if N==2:
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l]+nums[r]
                if s==target:
                    results.append(result+[nums[l], nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    while l < r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(len(nums)-N+1):
                if nums[0]*N > target or nums[-1]*N < target:
                    break
                elif  i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)



a=Solution()
print(a.fourSum([-2,-2,-2,-2,-1,0,1,2,2,2,2], 0))
