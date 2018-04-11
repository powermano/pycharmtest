class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return

        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                break
        if i == 0:
            self.reverse(0, nums)
        # elif len(nums) - i == 1:
        #     nums[i - 1], nums[i] = nums[i], nums[i - 1]

        else:
            for j in range(len(nums) - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    break
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            self.reverse(i, nums)

    def reverse(self, k, num):
        for i in range((len(num) - k) // 2):
            num[k + i], num[len(num) - 1 - i] = num[len(num) - 1 - i], num[k + i]
        return num
test = [1,2,3]
a = Solution()
a.nextPermutation(test)
print(test)