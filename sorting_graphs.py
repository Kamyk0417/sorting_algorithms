import matplotlib.pyplot as plt
import sorting
from random import randint

alg = input("bubble, quick, merge, insert, bucket, heap or all : ")

x = []
y = []

for j in range(100, 10000, 100):
    mean = 0
    x.append(j)
    for i in range(10):
        rndarray = [randint(1, 100) for k in range(j)]
        match alg:
            case "bubble": 
                time = sorting.time_measure(sorting.bubble_sort)(rndarray)
            case "quick": 
                time = sorting.time_measure(sorting.quick_sort)(rndarray)        
            case "merge": 
                time = sorting.time_measure(sorting.merge_sort)(rndarray)
            case "insert":
                time = sorting.time_measure(sorting.insert_sort)(rndarray)
            case "bucket":
                time = sorting.time_measure(sorting.bucket_sort)(rndarray)
            case "heap":
                time = sorting.time_measure(sorting.heap_sort)(rndarray)
        mean += time[1]
    y.append(mean/10)

plt.scatter(x, y)
plt.title("average time needed to sort an array depending on its length")
plt.xlabel("length of the array")
plt.ylabel("time needed to sort")
plt.show()



    

