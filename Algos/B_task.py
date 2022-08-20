import pandas as pd
import numpy as np
def multiple_push_back(arr, ci, xi):
    x_list = [xi] * ci
    arr.extend(x_list)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while  i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr

lst_size, m_func, k = list(map(int, input().split()))
if lst_size > 0:
    arr = list(map(int, input().split()))

    for m in range(m_func):
        ci, xi = list(map(int, input().split()))
        arr = multiple_push_back(arr, ci, xi)
    sorted_arr = merge_sort(arr)
    print(sorted_arr[k-1])