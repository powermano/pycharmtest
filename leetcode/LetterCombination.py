from functools import reduce
from time import ctime
class Solution(object):
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
        res = ['']
        # f = lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]]
        # for i in range(len(digits)):
        #     res = f(res, digits[i])
        # return res
        ret = [c for c in kvmaps[digits[0]]]
        for d in digits[1:]:
            res = []
            for s in ret:
                for c in kvmaps[d]:
                    res.append(s + c)
            ret = res
        return ret
# print(ctime())
a = Solution()
print(a.letterCombinations('23'))
# print(ctime())
