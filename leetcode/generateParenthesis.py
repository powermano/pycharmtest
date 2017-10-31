class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right - 1)
            if not right:    parens += p,
            return parens

        return generate('', n, n)


    # def generateParenthesis(self, n):
    #     def generate(p, left, right):
    #         if right >= left >= 0:
    #             if not right:
    #                 yield p
    #             # for q in generate(p + '(', left - 1, right): yield q
    #             # for q in generate(p + ')', left, right - 1): yield q
    #             yield from generate(p + '(', left - 1, right)
    #             yield from generate(p + ')', left, right - 1)
    #
    #     return list(generate('', n, n))


a = Solution()
print(a.generateParenthesis(2))
