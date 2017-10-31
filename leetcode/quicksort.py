class Solution(object):
    def quicksort1(self,nums, low, high):
        p = nums[low]
        while low < high:
            while low < high and nums[high] > p:
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]

            while low < high and nums[low] < p:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]

            # high -= 1
        # self.quicksort(nums[0:low+1], 0, low)
        # self.quicksort(nums[low+1:],low+1, len(nums))
        return low

    def quicksort(self, v, left, right):
        if left < right:
            p = self.quicksort1(v, left, right)
            self.quicksort(v, left, p)
            self.quicksort(v, p+1, right)


a = Solution()
array = [3,6,5,4,2,7,1,9,8]
print(a.quicksort1([3,6,5,4,2,7,1,9,8],0,8))
a.quicksort(array, 0, len(array)-1)
print(array)
