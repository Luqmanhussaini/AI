from collections import deque
def solve(a,b,ans):
    d={}
    solution=False
    paths=[]
    queue=deque()
    queue.append([0,0])
    while(len(queue)>0):
        cur=queue.popleft()
        
        if (cur[0],cur[1]) in d:
            continue
            
        if cur[0]<0 or cur[1]<0 or cur[0]>a or cur[1]>b :
            continue
            
        paths.append((cur[0],cur[1]))
        
        d[(cur[0],cur[1])]=1
        
        if cur[0]==ans or cur[1]==ans:
            solution= True
            if cur[0]==ans:
                if cur[1]!=0:
                    paths.append((cur[0],0))
            if cur[1]==ans:
                if cur[0]!=0:
                    paths.append((0,cur[1]))
                    
                    
            for i in range(len(paths)):
                print(paths[i][0]," ",paths[i][1],end="\n")
            break
            
        queue.append([cur[0],b])
        queue.append([a,cur[1]])
        
        for ml in range(max(a,b)+1):
            x=cur[0]+ml
            y=cur[1]-ml
            
            if x==a or y==0:
                queue.append([x,y])
                
            x=cur[0]-ml
            y=cur[1]+ml
            
            if x==0 or y==b:
                queue.append ([x,y])
            queue.append([a,0])
            queue.append([0,b])
    if (not solution):
        print("no solution")
        
            
            
            
            
            
# water jug prblm- bfs
j1=int(input())
j2=int(input())
final=int(input())

solve(j1,j2,final)
