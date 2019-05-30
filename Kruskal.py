class Graph:
    def __init__(self,vertices):
        self.graph=[]
        self.v=vertices
    def addedge(self,u,v,c):
        self.graph.append([u,v,c])
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        elif rank[yroot]>rank[xroot]:
            parent[xroot]=yroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
    def kruskal(self):
        (res,i,e)=([],0,0)
        self.graph=sorted(self.graph,key=lambda x:x[2])
        (parent,rank)=([],[])
        for j in range(self.v):
            parent.append(j)
            rank.append(0)
        while e<self.v-1:
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e+=1
                res.append([u,v,w])
                self.union(parent,rank,x,y)
        print('Edge\tWeight')
        sum=0
        for u,v,w in res:
            print('%d-%d\t\t%d'%(u,v,w))
            sum+=w
        print('Total min cost:',sum)
n=int(input('Enter no of vertices: '))
e=int(input('Enter no of edges: '))
g=Graph(n)
for i in range(e):
    u,v,cost=input('Enter an edge(u,v) and its cost(eg, u v cost): ').split()
    u=int(u)
    v=int(v)
    cost=int(cost)
    g.addedge(u,v,cost)
g.kruskal()
