# import math
#
#
# def all_factor(x):
#     a = []
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             a.append(i)
#             if (x // i) != i:
#                 a.append(x // i)
#     return a
#
#
#
#
#
# def solution(n, m):
#     # divs = [[] for _ in range(m + 1)]
#     # for i in range(2, m + 1):
#     #     for j in range(i + i, m + 1, i):
#     #         divs[j].append(i)
#     # for i in range(2, m + 1):
#     #     divs[i] = all_factor(i)
#
#     value = [m] * (m + 1)
#     value[n] = 0
#     for i in range(n, m + 1):
#         if value[i] < m:
#             for x in all_factor(i):
#             # for x in divs[i]:
#                 if i + x < m + 1:
#                     value[i + x] = min([value[i + x], value[i] + 1])
#     if value[m] < m:
#         return value[m]
#     else:
#         return -1
#
#
# data = [int(i) for i in input().strip().split()]
# n = data[0]
# m = data[1]
#
# print(solution(n, m))


# def solution(n, m):
#     divs = [[] for _ in range(m + 1)]
#     for i in range(2, m + 1):
#         for j in range(i + i, m + 1, i):
#             divs[j].append(i)
#     # for i in range(2, m + 1):
#     #     divs[i] = all_factor(i)
#
#     value = [m] * (m + 1)
#     value[n] = 0
#     current = [n]
#     while current != []:
#         next = []
#         for x in current:
#             for move in divs[x]:
#                 if (x + move) <= m:
#                     if (x + move) not in next:
#                         next.append(x + move)
#                 if value[x] + 1 < value[x + move]:
#                     value[x + move] = value[x] + 1
#         current = next
#     if value[m] < m:
#         return value[m]
#     else:
#         return -1
#
#
# data = [int(i) for i in input().strip().split()]
# n = data[0]
# m = data[1]
#
# print(solution(n, m))


def solution(a, b):
    divs = [[] for _ in range(b + 1)]
    for i in range(2, b + 1):
        for j in range(i + i, b + 1, i):
            divs[j].append(i)
    # using BFS
    seen = set([a])
    par, child = [a], []
    depth = 0
    while par:
        depth += 1
        for p in par:
            for f in divs[p]:
                temp = f + p
                if temp not in seen:
                    seen.add(temp)
                    if temp == b:
                        return depth
                    elif temp < b:
                        child.append(f + p)
        par, child = child, []
    return -1


a, b = map(int, input().split())
if a == 2:
    print(-1)
elif a == b:
    print(0)
elif b - a == 1:
    print(-1)
else:
    print(solution(a, b))