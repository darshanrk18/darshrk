def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
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
    return C

def mergesort(A,left,right):
    if right-left<=1:
        return A[left:right]
    mid=(left+right)//2
    L=mergesort(A,left,mid)
    R=mergesort(A,mid,right)
    return merge(L,R)

print("Enter the list of elements to be sorted: ",end=' ')
A=[int(x) for x in input().split()]
A=mergesort(A,0,len(A))
print("Sorted list:")
for i in A:
    print(i,end=' ')
print()
