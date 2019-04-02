from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,s):
        visited=[]
        queue=[]
        queue.append(s)
        visited.append(s)
        while queue!=[]:
            s=queue.pop(0)
            print(s,end=' ')
            for i in self.graph[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print()
n=int(input("Enter no. of edges: "))
g=Graph()
for i in range(n):
    a,b=input("Enter an edge: ").split()
    #a=int(a)
    #b=int(b)
    g.addedge(a,b)
s=(input("Enter the source vertex: "))
print("BFS".center(11,'*'))
g.BFS(s)
