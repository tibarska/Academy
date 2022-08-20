n = int(input())
arr = [int(i) for i in input().split()]

x = max(arr)

best = x / 2

diffs = [i - best for i in arr]

abs_diffs = [abs(i) for i in diffs]

min_abs_diff = min(abs_diffs)

if min_abs_diff in diffs:
    y = best + min_abs_diff
else:
    y = best - min_abs_diff
y = int(y)
print(x, y)