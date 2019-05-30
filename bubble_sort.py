import random
import time


def bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                (array[i],array[j]) = (array[j],array[i])
    print(array)


no_of_elements = int(input("Enter number of elements : "))
array = []
for i in range(no_of_elements):
    array.append(random.randint(0, 100))
print("Before Sorting")
print(array)
print("After sorting")
start = time.time()
bubble_sort(array)
end = time.time()
print("Execution time : ",end-start)

