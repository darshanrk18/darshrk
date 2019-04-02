from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=[]
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self,s):
        self.visited.append(s)
        print(s,end=' ')
        for i in self.graph[s]:
            if i not in self.visited:
                self.visited.append(i)
                self.DFS(i)
g=Graph()
n=int(input("Enter no. of edges: "))
for i in range(n):
    a,b=input("Enter an edge: ").split()
    #a=int(a)
    #b=int(b)
    g.addedge(a,b)
s=(input("Enter a source vertex: "))
print("DFS".center(11,'*'))
g.DFS(s)
print()
