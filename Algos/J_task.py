rows, cols = list(map(int, input().split()))

grid = []
for i in range(rows):
    s = input()
    s = [x for x in s]
    grid.append(s)
steps = [[0]*(cols+1) for j in range(rows)]

if grid[0][0] == '#':
    steps[0][1] = 1
    steps[1][0] = 1
i = 0
for j in range(1, cols):
    if grid[i][j] == '#':
        steps[i][j+1] = steps[i][j] + 1
    else:
        steps[i][j+1] = steps[i][j]

for i in range(1, rows):
    for j in range(cols):
        if j == 0:
            if grid[i][j] == '.':
                steps[i][1] = steps[i-1][1]
            if grid[i][j] == '#':
                steps[i][1] = steps[i-1][1] +1
        else:
            if grid[i][j] == '.':
                steps[i][j+1] = min(steps[i-1][j+1], steps[i][j])
            else:
                steps[i][j+1] = min(steps[i-1][j+1], steps[i][j]) + 1
print(steps[-1][-1])