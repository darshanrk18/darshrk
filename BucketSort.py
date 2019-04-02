import math
import string
import random
DEFAULT_BUCKET_SIZE = 5
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        while i>0 and arr[i]<arr[i-1]:
            (arr[i-1],arr[i],i)=(arr[i],arr[i-1],i-1)

def sort(array, bucketSize=DEFAULT_BUCKET_SIZE):
    f=0
    if type(array)==str:
        f=1
        array=[ord(x) for x in array]
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
              maxValue = array[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    #Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

    #Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    if f:
        for i in range(len(array)):
            print(chr(array[i]),end=' ')
    else:
        for i in range(0, len(array)):
            print(array[i],end=' ')

c=int(input("1.Str input\n2.Int input\n3.Float input\nEnter your choice: "))
if c==1:
    l=[random.choice(string.ascii_uppercase) for x in range(10)]
elif c==2:
    l=[random.randint(1,100) for x in range(10)]
else:
    l=[float('%.2f'%random.uniform(1,3)) for x in range(10)]
print("Initial list:",l)
print("SORTED LIST".center(51,'*'))
sort(l)
print()
