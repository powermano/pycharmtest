# n, m, p = map(int, input().split())
# amap = [list(map(int, input().split())) for i in range(n)]
# visited = [[0] * m for i in range(n)]
# step = [[0] * m for i in range(n)]
# min = 100000
# current_path = [[0, 0]]
# final_path = []
# min_path = []
# move = [[-1,0],[0,-1],[0,1],[1,0]]
# consume = [3, 1, 1, 0]
# while current_path != []:
#     temp = current_path.pop()
#     final_path.append(temp)
#     x0 = temp[0]
#     y0 = temp[1]
#     visited[x0][y0] = 1
#     flag = 0
#     for i in range(len(move)):
#         if (x0 + move[i][0]) >= n or (x0 + move[i][0]) < 0 or (y0 + move[i][1]) >= m or (y0 + move[i][1]) < 0: continue
#         if amap[x0 + move[i][0]][y0 + move[i][1]] != 1 or visited[x0 + move[i][0]][y0 + move[i][1]] == 1 or step[x0][y0] + consume[i] > p: continue
#         step[x0 + move[i][0]][y0 + move[i][1]] = step[x0][y0] + consume[i]
#         current_path.append([x0 + move[i][0],y0 + move[i][1]])
#         # visited[x0 + move[i][0]][y0 + move[i][1]] = 1
#         flag = 1
#         if (x0 + move[i][0]) == 0 and (y0 + move[i][1]) == (m - 1) and step[x0 + move[i][0]][y0 + move[i][1]] < min:
#             min = step[x0 + move[i][0]][y0 + move[i][1]]
#             min_path = final_path[:]
#             min_path.append([x0 + move[i][0],y0 + move[i][1]])
#             visited[x0 + move[i][0]][y0 + move[i][1]] = 0
#             current_path.pop()
#             if current_path != []:
#                 while final_path != []:
#                     if (abs(current_path[-1][0] - final_path[-1][0]) + abs(
#                             current_path[-1][1] - final_path[-1][1])) > 1:
#                         s = final_path.pop()
#                         visited[s[0]][s[1]] = 0
#                     else: break
#                 break
#     if flag == 0:
#         final_path.pop()
#         if current_path != []:
#             while final_path != []:
#                 if (abs(current_path[-1][0] - final_path[-1][0]) + abs(current_path[-1][1] - final_path[-1][1])) > 1:
#                     final_path.pop()
#                 else: break
#
# if min == 100000:
#     print('Can not escape!')
# for i in range(len(min_path)):
#     if i != len(min_path) - 1:
#         print('[%d,%d]'%(min_path[i][0],min_path[i][1]), end=',')
#     else: print('[%d,%d]'%(min_path[i][0],min_path[i][1]), end='\n')

import sys

n, m, p = map(lambda x: int(x), input().split())
amap = []
reached = []
possibalepath = []
possibalep = -1
current_path = []
for loop1 in range(int(n)):
    input1 = input().split()
    amap.append(input1)

    temprow = []
    for loop2 in range(len(input1)):
        temprow.append(False)
    reached.append(temprow)


def can_continue(i, j, p):
    if i < 0 or i >= n or j < 0 or j >= m or p < 0 or reached[i][j] or amap[i][j] == '0':
        return False
    return True


def search(i, j, p):
    current_path.append([i, j])
    reached[i][j] = True
    global possibalep
    if i == 0 and j == m - 1 and p > possibalep:
       # global possibalepath
        possibalepath = current_path[:]
        possibalep = p
        current_path.pop()
        reached[i][j] = False
        return
    reached[i][j] = True
    if can_continue(i - 1, j, p - 3):
        search(i - 1, j, p - 3)
    if can_continue(i + 1, j, p):
        search(i + 1, j, p)
    if can_continue(i, j + 1, p - 1):
        search(i, j + 1, p - 1)
    if can_continue(i, j - 1, p - 1):
        search(i, j - 1, p - 1)
    current_path.pop()
    reached[i][j] = False
    return


search(0, 0, p)

if possibalep == -1:
    print ("Can not escape!")
else:
    for i in range(len(possibalepath)):
        if i != len(possibalepath) - 1:
            print('[%d,%d]'%(possibalepath[i][0],possibalepath[i][1]), end=',')
        else: print('[%d,%d]'%(possibalepath[i][0],possibalepath[i][1]), end='\n')
