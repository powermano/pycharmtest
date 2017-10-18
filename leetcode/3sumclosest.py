class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        m = nums[0] + nums[1] + nums[2] - target
        rv = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r] - target
                if abs(s) < abs(m):
                    m = s
                    rv = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                if s < 0:
                    l += 1
                if s == 0:
                    return target
        return rv
s= Solution()
print(s.threeSumClosest([-3,-2,-5,3,-4], -1))

[-3,-2,-5,3,-4]
-1