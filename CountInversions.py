import random
def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j,c)=(0,0,0)
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j+=1
        elif j==n:
            C.append(A[i])
            i+=1
        elif A[i]<=B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
            c+=len(A)-i
    return (C,c)

def mergesort(A,left,right):
    if right-left<=1:
        return (A[left:right],0)
    mid=(left+right)//2
    (L,ca)=mergesort(A,left,mid)
    (R,cb)=mergesort(A,mid,right)
    (res,c)=merge(L,R)
    c+=ca+cb
    return (res,c)

'''print("Enter the list of elements to be sorted: ",end=' ')
A=[int(x) for x in input().split()]'''
A=[random.randint(1,50) for x in range(1,10)]
print("List:",A)
(A,c)=mergesort(A,0,len(A))
print("Sorted list:")
for i in A:
    print(i,end=' ')
print("\nNo. of inversions:",c)
