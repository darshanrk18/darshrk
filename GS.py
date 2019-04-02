mp={}
wp={}
n=int(input("Enter no. of men and women: "))
freemen=[]
for i in range(n):
    name=input("Enter the name of man: ")
    freemen.append(name)
    print("Enter his preference list: ",end=' ')
    l=list(input().split())
    mp[name]=l
for i in range(n):
    name=input("Enter the name of woman: ")
    print("Enter her preference list: ",end=' ')
    l=list(input().split())
    wp[name]=l
taken=[]
final={}
while freemen!=[]:
    for i in freemen:
        listofw=mp.get(i)
        for j in listofw:
            if j not in taken:
                freemen.remove(i)
                taken.append(j)
                final[j]=i
                break
            else:
                listofm=wp.get(j)
                r=final[j]
                p=listofm.index(i)
                q=listofm.index(r)
                if p<q:
                    freemen.append(r)
                    freemen.remove(i)
                    final[j]=i
                    break
print(final)
