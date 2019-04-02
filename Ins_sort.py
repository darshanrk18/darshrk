def insort(l):
    for i in range(1,len(l)):
        while i>0 and l[i]<l[i-1]:
            (l[i-1],l[i],i)=(l[i],l[i-1],i-1)

print("Enter the list to be sorted",end=' ')
l=[int(x) for x in input().split()]
insort(l)
print(l)
