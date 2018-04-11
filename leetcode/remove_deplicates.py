class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(nums)):
            if nums[i-count] == nums[i-count-1]:
                nums.pop(i-count)
                count += 1
        return nums

a = Solution()
list = [1,1,2,2,3,4]
b = a.removeDuplicates(list)
print(b)
