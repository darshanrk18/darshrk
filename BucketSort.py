import math
DEFAULT_BUCKET_SIZE = 5
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        while i>0 and arr[i]<arr[i-1]:
            (arr[i-1],arr[i],i)=(arr[i],arr[i-1],i-1)

def sort(array, bucketSize=DEFAULT_BUCKET_SIZE):
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
    bucketCount = math.floor((ord(maxValue) -ord( minValue)) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    #Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((ord(array[i]) -ord( minValue)) / bucketSize)].append(array[i])

    #Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    for i in range(0, len(array)):
        print(array[i])

print("Enter the list of elements to be sorted: ",end=' ')
l=[(x) for x in input().split()]
sort(l)
