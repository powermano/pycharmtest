n = int(input())
a = input().strip().split()
for i in range(n):
    a[i] = int(a[i])
b = input().strip().split()
k = int(b[0])
d = int(b[1])
p = [[0] * (n + 1) for i in range(k + 1)]
f = [[0] * (n + 1) for i in range(k + 1)]
for i in range(1,k + 1):
    for j in range(1,n + 1):
        if i > j:
            p[i][j] = 0
            f[i][j] = 0
        if i == j:
            temp = 1
            for l in range(j):
                temp *= a[l]
            p[i][j] = temp
            f[i][j] = temp
        if i < j:
            max1 = max((a[j - 1] * p[i - 1][j - 1]), (a[j - 1] * f[i - 1][j - 1]))
            min1 = min((a[j - 1] * p[i - 1][j - 1]), (a[j - 1] * f[i - 1][j - 1]))
            for m in range(1, min(d,n) + 1):
                if (j - m) > 0:
                    if (i - 1) == 0: max1 = min1 = a[j - 1]
                    max1 = max((a[j - 1] * p[i - 1][j - m]), (a[j - 1] * f[i - 1][j - m]), max1)
                    min1 = min((a[j - 1] * p[i - 1][j - m]), (a[j - 1] * f[i - 1][j - m]), min1)
            p[i][j] = max1
            f[i][j] = min1
maxvalue = 0
for i in range(len(p)):
    if max(p[i]) > maxvalue: maxvalue = max(p[i])
print(maxvalue)