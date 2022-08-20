n, m, T = list(map(int, input().split()))
times = []
for i in range(n):
    time = int(input())
    times.append(time)

times = sorted(times)
waiting_time = [time + T for time in times]


class MinStack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        push_min = min(value, self.lst[-1][1]) if len(self.lst) else value
        self.lst.append((value, push_min))

    def pop(self):
        return self.lst.pop()[0]

    def get_min(self):
        return self.lst[-1][1]

    def __len__(self):
        return len(self.lst)


calls = 0
orders = MinStack()
orders.push(waiting_time[0])

for i in range(1, len(times)):
    min_waiting = orders.get_min()
    if min_waiting >= times[i] and len(orders) < m:
        orders.push(waiting_time[i])
    elif min_waiting >= times[i] and len(orders) == m:
        for j in range(m):
            orders.pop()
        calls += 1
        orders.push(waiting_time[i])
    else:
        for j in range(len(orders)):
            orders.pop()
        calls += 1
        orders.push(waiting_time[i])

if len(orders) > 0:
    calls += 1
print(calls)