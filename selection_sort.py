import random
import time


def selection_sort(array):
    for i in range(0,len(array)-1):
        key = i
        for j in range(i+1,len(array)):
            if array[key] > array[j]:
                key = j
        (array[i],array[key]) = (array[key],array[i])
    print(array)


no_of_elements = int(input("Enter number of elements : "))
array = []
for i in range(no_of_elements):
    array.append(random.randint(0, 100))
print("Before Sorting")
print(array)
print("After Sorting")
start = time.time()
selection_sort(array)
end = time.time()
print("Execution time :",end-start)


