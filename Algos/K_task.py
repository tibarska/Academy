n, m = [int(i) for i in input().split()]
field = [list(input()) for _ in range(n)]
steps = [[1000000]*(m+1) for _ in range(n+1)]
steps[0][1] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if field[i-1][j-1]=='.':
            steps[i][j] = min(steps[i-1][j], steps[i][j-1])
        else:
            up = steps[i-1][j]
            if i - 2 >= 0 and field[i-2][j-1] == '#':
                up -= 1
            lf = steps[i][j-1]
            if j - 2 >= 0 and field[i-1][j-2] == '#':
                lf -= 1
            steps[i][j] = min(up, lf) + 1
print(steps[-1][-1])