borders = {'|': 1, "\\": 2, '/': 3}
shapes = {'a': 1, 'A': 2, 'b': 1, 'B': 2, 'c': 1, 'C': 2, '1': 3, '2': 3, '3': 3}
colors = {'a': 1, 'b': 2, 'c': 3, '1': 1, '2': 2, '3': 3, 'A': 1, 'B': 2, 'C': 3}

n = int(input())
all_elements = []
cnt_elements = {}
for i in range(n):
    el = input()
    border = borders.get(el[:1])
    shape = shapes.get(el[1:2])
    color = colors.get(el[1:2])
    size = len(el[1:-1])
    all_elements.append((border, shape, color, size))
    cnt_elements[(border, shape, color, size)] = cnt_elements.get((border, shape, color, size), 0) + 1

set_dict = {}
from itertools import combinations

if len(all_elements) >= 3:
    for trio in combinations(all_elements, 3):
        x1, y1, z1, w1 = trio[0]
        x2, y2, z2, w2 = trio[1]
        x3, y3, z3, w3 = trio[2]
        if (x1 == x2 == x3 or x1 + x2 + x3 == 6) and (y1 == y2 == y3 or y1 + y2 + y3 == 6) and (
                z1 == z2 == z3 or z1 + z2 + z3 == 6) and (w1 == w2 == w3 or w1 + w2 + w3 == 6):
            set_dict[(x1, y1, z1, w1)] = set_dict.get((x1, y1, z1, w1), 0) + 1
            set_dict[(x2, y2, z2, w2)] = set_dict.get((x2, y2, z2, w2), 0) + 1
            set_dict[(x3, y3, z3, w3)] = set_dict.get((x3, y3, z3, w3), 0) + 1
    for element in all_elements:
        x, y, z, w = element
        print(int(set_dict.get((x, y, z, w)) / cnt_elements.get((x, y, z, w))))
else:
    for element in all_elements:
        print(0)