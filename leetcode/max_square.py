class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        n = len(matrix[0])
        heights = [0] * (len(matrix[0]) + 1)
        ans = 0

        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    temp = min(h, w)
                    ans = max(ans, temp * temp)
                stack.append(i)

        return ans

a = Solution()
test = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(a.maximalSquare(test))

