#read data from console

n, m = map(int, input().split())
# number = list(map(int, input().split()))
# a = [list(map(int, input().split())) for i in range(m)]
b = [[int(x) for x in input().split()] for _ in range(m)]
print(b)

# A = [None for i in range(10)]
# N = 3
#
# def dfs(cur):
#     if cur == N:
#         print(A[:N])
#     else:
#         for i in range(1, N+1):
#             if i not in A[:cur]:
#                 A[cur] = i
#                 dfs(cur+1)
#
# dfs(0)

# A = [None for i in range(0, 10)]
# N = 6
#
# def is_prime(n):
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             return False
#     return True
#
# def dfs(cur):
#     if cur == N:
#         if is_prime(A[0]+A[N-1]):
#             print(A[:N])
#     else:
#         for i in range(1, N+1):
#             if i not in A[:cur]:
#                 if cur == 0 or is_prime(i+ A[cur-1]):
#                     A[cur] = i
#                     dfs(cur+1)
#
# dfs(0)

# Q = [None for i in range(0, 8)]
# CNT = 0
# N = 8
#
# def dfs(cur):
#     if cur == N:
#         global CNT
#         CNT += 1
#     else:
#         for i in range(0, N):
#             Q[cur] = i
#             ok = True
#             for j in range(0, cur):
#                 if Q[cur]==Q[j] or cur-Q[cur]==j-Q[j] or cur+Q[cur]==j+Q[j]:
#                     ok = False
#             if ok:
#                 dfs(cur+1)
#
#
# dfs(0)
# print('ans = ' + str(CNT))