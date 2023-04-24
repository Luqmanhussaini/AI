# uniform cost
from collections import deque
graph={}
n=int(input())
for i in range(n):
    node=int(input("node:"))
    child=int(input("no.of child: "))
    sub={}
    for i in range(child):
        d=int(input("destiny:"))
        c=int(input("cost: "))
        sub[d]=c
    graph[node]=sub
        
graph
visited=[False]*n
uniform_cost(graph,visited)


def uniform_cost(graph,visited):
    
    
    
