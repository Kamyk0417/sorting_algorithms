import matplotlib.pyplot as plt
from sorting import *
from random import randint

alg = input("bubble, quick, merge, insert, bucket, heap or compare: ")
if alg == "compare":
    comp1 = input("Choose 1st: ")
    comp2 = input("Choose 2nd: ")

alg_dict = {"bubble": bubble_sort, "quick": quick_sort, "merge": merge_sort, 
            "insert": insert_sort, "bucket": bucket_sort, "heap": heap_sort}

def compare(alg1,alg2):
    x, y1, y2 = [],[],[]
    for j in range(100, 10000, 100):
        mean1 = 0
        mean2 = 0
        x.append(j)
        for i in range(1):
            rndarray = [randint(1, 100) for k in range(j)]
            time1 = alg1(rndarray)
            time2 = alg2(rndarray)
            mean1 += time1[1]
            mean2 += time2[1]
        y1.append(mean1)
        y2.append(mean2)

    return x, y1, y2

x = []
y = []

if alg != "compare":
    for j in range(100, 10000, 100):
        mean = 0
        x.append(j)
        for i in range(1):
            rndarray = [randint(1, 100) for k in range(j)]
            time_dec = time_measure(alg_dict[alg])(rndarray)
            mean += time_dec[1]
        y.append(mean)
    plt.scatter(x,y)

if alg == "compare":
    ox, val1, val2 = compare(time_measure(alg_dict[comp1]), time_measure(alg_dict[comp2]))
    plot1 = plt.scatter(ox,val1)
    plot2 = plt.scatter(ox,val2)
    plt.legend((plot1,plot2), (comp1, comp2))

plt.title("average time needed to sort an array depending on its length")
plt.xlabel("length of the array")
plt.ylabel("time needed to sort")
plt.show()



    

