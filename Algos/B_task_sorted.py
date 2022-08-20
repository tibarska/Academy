def multiple_push_back(arr, ci, xi):
    global el_dict
    el_dict[xi] = ci + el_dict.get(xi, 0)
    return el_dict

lst_size, m_func, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

el_dict = {}
for el in arr:
    el_dict[el] = 1 + el_dict.get(el, 0)

for m in range(m_func):
    ci, xi = list(map(int, input().split()))
    multiple_push_back(arr, ci, xi)

dict_keys = list(el_dict.keys())
dict_keys = sorted(dict_keys)
idx = 0
for key in dict_keys:
    cnt = el_dict[key]
    idx += cnt
    if idx >= k:
        print(key)
        break