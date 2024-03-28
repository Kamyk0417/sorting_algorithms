import random
from time import time 


def time_measure(func):
    def measured(*args,**kwargs):
        start = time()
        val = func(*args,**kwargs)
        stop = time()
        return val, stop-start
    return measured


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def merge_sort(arr):
    if len(arr) > 1:

        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        merge_sort(left)
        merge_sort(right)
    
        r_i, l_i, i = 0,0,0 
    
        while r_i < len(right) and l_i < len(left):
            if right[r_i] < left[l_i]:
                arr[i] = right[r_i]
                r_i += 1
            else: 
                arr[i] = left[l_i]
                l_i += 1
            i += 1

        while r_i < len(right):
            arr[i] = right[r_i]
            r_i += 1
            i += 1

        while l_i < len(left):
            arr[i] = left[l_i]
            l_i += 1
            i += 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left)+mid+quick_sort(right)


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def bucket_sort(arr):
    max_val = max(arr)
    buckets_nr = max_val//10+1

    buckets = [[] for _ in range(buckets_nr)]

    for num in arr:
        bucket_index = num//10
        buckets[bucket_index].append(num)

    for b in buckets:
        insert_sort(b)

    sorted = []
    for b in buckets:
        sorted.extend(b)

    return sorted


def one_heap_sort(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] > arr[largest]:
        largest = left 
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        one_heap_sort(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        one_heap_sort(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        one_heap_sort(arr,i,0)
    

