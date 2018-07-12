def bsf():
    n, m = list(map(int, input().strip().split()))
    a = [input() for i in range(n)]
    x0, y0 = list(map(int, input().strip().split()))
    k = int(input())
    x = [list(map(int, input().strip().split())) for i in range(k)]
    #x = [[int(s) for s in input().split()] for i in range(k)] also works
    step = [[-1] * m for i in range(n)]
    visit = [[0] * m for i in range(n)]
    current = [[x0,y0]]
    step[x0][y0] = 0
    visit[x0][y0] = 1
    while current != []:
        next = []
        for s in current:
            x0 = s[0]
            y0 = s[1]
            for move in x:
                if (x0 + move[0]) >= n or (x0 + move[0]) < 0 or (y0 + move[1])  >= m or (y0 + move[1]) < 0: continue
                if a[x0 + move[0]][y0 + move[1]] != '.'or visit[x0 + move[0]][y0 + move[1]] == 1: continue
                else:
                    visit[x0 + move[0]][y0 + move[1]] = 1
                    step[x0 + move[0]][y0 + move[1]] = step[x0][y0] + 1
                    next.append([x0 + move[0], y0 + move[1]])
        current = next
    maxvalue = 0
    for i in range(n):
        for j in range(m):
            if step[i][j] == -1 and a[i][j] == '.':
                return -1
            maxvalue = max(maxvalue, step[i][j])
    return maxvalue
