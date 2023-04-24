# depth limit search
limit=int(input("limit"))
temp=limit
def final(ans):
    print(ans)
    exit()
def dfs(start,visited,graph,limit,ans):
    
    visited.add(start)
    ans.append(start)
    if start==goal:
        final(ans)
#     print(start)
    limit-=1
    for i in graph[start]:    
        if limit ==0:
            limit=temp
            break
        if i not in visited:
            dfs(i,visited,graph,limit,ans)

    
from collections import deque
n=int(input("n"))

start=input("start")
goal=input("goal")
q=deque()
graph={}
ans=[]
for i in range(n):
    node=input("node")
    child=int(input("child"))
    l=[]
    for k in range(child):
       l.append(input("l: "))
    graph[node]=l
print(graph)
q.append(start)
visited=set()
dfs(start,visited,graph,limit,ans)
      
                
           
