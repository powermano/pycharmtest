# x = input()
# y = input()
# m, n = len(x), len(y)
# p = [[0] * (n + 1) for i in range(m + 1)]
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         if x[i - 1] == y[j - 1]: p[i][j] = p[i - 1][j - 1] + 1
#         else: p[i][j] = max(p[i - 1][j], p[i][j - 1])
# if p[m][n] == min(m,n): print('Yes')
# else: print('No')


# import re
# str1 = input()
# str2 = input()
# item = ""
# for i in str2:item +=".*"+i
# item += ".*"
# if re.search(item, str1):print("Yes")
# else:print("No")

x = input()
y = input()
t = 0
f = 1
for str in y:
    if (x.find(str,t) == -1):
        f = 0
        break
    else: t = x.find(str, t) + 1
if f == 1: print('Yes')
if f == 0: print("No")