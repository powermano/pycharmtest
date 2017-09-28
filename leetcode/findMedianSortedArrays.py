# def median(A, B):
#     m, n = len(A), len(B)
#     if m > n:
#         A, B, m, n = B, A, n, m  ##do not to use swap
#     if n == 0:
#         raise ValueError
#
#     imin, imax, half_len = 0, m, (m + n + 1) // 2
#     while imin <= imax:
#         i = (imin + imax) // 2
#         j = half_len - i
#         if i < m and B[j-1] > A[i]:
#             # i is too small, must increase it
#             imin = i + 1
#         elif i > 0 and A[i-1] > B[j]:
#             # i is too big, must decrease it
#             imax = i - 1
#         else:
#             # i is perfect
#
#             if i == 0: max_of_left = B[j-1]
#             elif j == 0: max_of_left = A[i-1]
#             else: max_of_left = max(A[i-1], B[j-1])
#
#             if (m + n) % 2 == 1:
#                 return max_of_left
#
#             if i == m: min_of_right = B[j]
#             elif j == n: min_of_right = A[i]
#             else: min_of_right = min(A[i], B[j])
#
#             return (max_of_left + min_of_right) / 2.0
#
# nums1 = [1, 2]
# nums2 = [3, 4]
# b=median(nums1, nums2)
# print(b)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n =len(nums1), len(nums2)
        if len(nums1) > len(nums2):
            m, n, nums1, nums2 = len(nums2), len(nums1), nums2, nums1


        lmin, lmax, half = 0, m, (m + n + 1) // 2
        while lmin <= lmax:
            i = (lmin + lmax) // 2
            j = half -i
            if i < m and nums2[j - 1] > nums1[i]:
                lmin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                lmax = i - 1

            else:

                if i == 0: max_left=nums2[j-1]
                elif j == 0: max_left=nums1[i-1]
                else: max_left=max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

nums1 = [1, 2]
nums2 = [3, 4]

a= Solution()
b=a.findMedianSortedArrays(nums1,nums2)
print(b)